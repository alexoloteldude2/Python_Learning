"use client";

import { useEffect, useState, useCallback } from "react";
import { useRouter } from "next/navigation";
import { format } from "date-fns";
import { zhCN } from "date-fns/locale";
import {
  BookOpen,
  CalendarDays,
  ChevronLeft,
  ChevronRight,
  LogOut,
  RefreshCw,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { TaskCard } from "@/components/TaskCard";
import { AddTaskDialog } from "@/components/AddTaskDialog";
import { ProgressDashboard } from "@/components/ProgressDashboard";
import { SUBJECT_CONFIG, SUBJECTS, todayString, getWeekDates } from "@/lib/utils";
import { Task } from "@/lib/supabase";

type ViewMode = "day" | "week";

export default function DashboardPage() {
  const router = useRouter();
  const [viewMode, setViewMode] = useState<ViewMode>("day");
  const [selectedDate, setSelectedDate] = useState<string>(todayString());
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [calOpen, setCalOpen] = useState(false);

  const weekDates = getWeekDates(selectedDate);

  // ── Fetch tasks ──────────────────────────────────────────────────
  const fetchTasks = useCallback(async () => {
    setLoading(true);
    try {
      const params =
        viewMode === "day"
          ? `?date=${selectedDate}`
          : `?week=${weekDates[0]}`;
      const res = await fetch(`/api/tasks${params}`);
      if (res.ok) {
        const data: Task[] = await res.json();
        setTasks(data);
      }
    } finally {
      setLoading(false);
    }
  }, [selectedDate, viewMode, weekDates[0]]);

  useEffect(() => {
    fetchTasks();
  }, [fetchTasks]);

  // ── Task operations ───────────────────────────────────────────────
  async function handleToggle(id: string, value: boolean) {
    // Optimistic update
    setTasks((prev) => prev.map((t) => (t.id === id ? { ...t, is_completed: value } : t)));
    await fetch(`/api/tasks/${id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ is_completed: value }),
    });
  }

  async function handleDelete(id: string) {
    setTasks((prev) => prev.filter((t) => t.id !== id));
    await fetch(`/api/tasks/${id}`, { method: "DELETE" });
  }

  function handleTaskAdded(task: Task) {
    const inRange =
      viewMode === "day"
        ? task.date === selectedDate
        : weekDates.includes(task.date);
    if (inRange) {
      setTasks((prev) => [...prev, task]);
    }
  }

  // ── Navigation ────────────────────────────────────────────────────
  function shiftDate(delta: number) {
    const d = new Date(selectedDate + "T00:00:00");
    d.setDate(d.getDate() + (viewMode === "day" ? delta : delta * 7));
    setSelectedDate(d.toISOString().split("T")[0]);
  }

  async function handleLogout() {
    await fetch("/api/auth/logout", { method: "POST" });
    router.push("/");
  }

  // ── Group tasks by subject (week mode) ───────────────────────────
  const tasksByDate = weekDates.reduce<Record<string, Task[]>>((acc, d) => {
    acc[d] = tasks.filter((t) => t.date === d);
    return acc;
  }, {});

  const dayTasks = tasks.filter((t) => t.date === selectedDate);
  const progressTasks = viewMode === "day" ? dayTasks : tasks;

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-50">
      {/* ── Header ── */}
      <header className="sticky top-0 z-30 bg-white/80 backdrop-blur-md border-b border-gray-200/60 shadow-sm">
        <div className="max-w-4xl mx-auto px-4 py-3 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-blue-600 flex items-center justify-center">
              <BookOpen className="w-4 h-4 text-white" />
            </div>
            <h1 className="font-bold text-gray-900 text-lg hidden sm:block">PSLE 复习计划</h1>
            <h1 className="font-bold text-gray-900 text-base sm:hidden">PSLE</h1>
          </div>

          <div className="flex items-center gap-2">
            {/* View mode toggle */}
            <div className="flex bg-gray-100 rounded-lg p-0.5">
              <button
                onClick={() => setViewMode("day")}
                className={`px-3 py-1.5 rounded-md text-xs font-medium transition-all ${
                  viewMode === "day"
                    ? "bg-white shadow text-blue-700"
                    : "text-gray-500 hover:text-gray-700"
                }`}
              >
                日视图
              </button>
              <button
                onClick={() => setViewMode("week")}
                className={`px-3 py-1.5 rounded-md text-xs font-medium transition-all ${
                  viewMode === "week"
                    ? "bg-white shadow text-blue-700"
                    : "text-gray-500 hover:text-gray-700"
                }`}
              >
                周视图
              </button>
            </div>

            <Button
              variant="ghost"
              size="icon"
              onClick={handleLogout}
              className="text-gray-500 hover:text-red-600"
              title="退出登录"
            >
              <LogOut className="w-4 h-4" />
            </Button>
          </div>
        </div>
      </header>

      {/* ── Main ── */}
      <main className="max-w-4xl mx-auto px-4 py-6 space-y-5">
        {/* Date navigator */}
        <div className="flex items-center gap-3">
          <Button variant="outline" size="icon" onClick={() => shiftDate(-1)} className="shadow-sm">
            <ChevronLeft className="h-4 w-4" />
          </Button>

          <Popover open={calOpen} onOpenChange={setCalOpen}>
            <PopoverTrigger asChild>
              <Button variant="outline" className="flex-1 sm:flex-none gap-2 shadow-sm font-medium">
                <CalendarDays className="h-4 w-4 text-blue-500" />
                {viewMode === "day"
                  ? format(new Date(selectedDate + "T00:00:00"), "yyyy年M月d日 (EEE)", {
                      locale: zhCN,
                    })
                  : `${format(new Date(weekDates[0] + "T00:00:00"), "M月d日", { locale: zhCN })} - ${format(
                      new Date(weekDates[6] + "T00:00:00"),
                      "M月d日",
                      { locale: zhCN }
                    )}`}
              </Button>
            </PopoverTrigger>
            <PopoverContent className="w-auto p-0">
              <Calendar
                mode="single"
                selected={new Date(selectedDate + "T00:00:00")}
                onSelect={(d) => {
                  if (d) {
                    setSelectedDate(d.toISOString().split("T")[0]);
                    setCalOpen(false);
                  }
                }}
                initialFocus
              />
            </PopoverContent>
          </Popover>

          <Button variant="outline" size="icon" onClick={() => shiftDate(1)} className="shadow-sm">
            <ChevronRight className="h-4 w-4" />
          </Button>

          <Button
            variant="ghost"
            size="icon"
            onClick={fetchTasks}
            disabled={loading}
            className="text-gray-400 hover:text-blue-600"
            title="刷新"
          >
            <RefreshCw className={`h-4 w-4 ${loading ? "animate-spin" : ""}`} />
          </Button>
        </div>

        {/* Progress + Add task row */}
        <div className="flex flex-col sm:flex-row gap-4">
          <div className="flex-1">
            <ProgressDashboard
              tasks={progressTasks}
              label={viewMode === "day" ? "今日" : "本周"}
            />
          </div>
          <div className="flex sm:flex-col justify-end sm:justify-start gap-2">
            <AddTaskDialog defaultDate={selectedDate} onTaskAdded={handleTaskAdded} />
            <Button
              variant="outline"
              size="sm"
              onClick={() => {
                setSelectedDate(todayString());
              }}
              className="text-xs"
            >
              回到今天
            </Button>
          </div>
        </div>

        {/* ── DAY VIEW ── */}
        {viewMode === "day" && (
          <Card className="shadow-md border-0">
            <CardHeader className="pb-3 border-b">
              <CardTitle className="text-base text-gray-700 flex items-center justify-between">
                <span>
                  {format(new Date(selectedDate + "T00:00:00"), "M月d日", { locale: zhCN })} 的任务
                </span>
                {dayTasks.length > 0 && (
                  <span className="text-xs font-normal text-gray-400">
                    共 {dayTasks.length} 项
                  </span>
                )}
              </CardTitle>
            </CardHeader>
            <CardContent className="pt-4">
              {loading ? (
                <div className="space-y-3">
                  {[1, 2, 3].map((i) => (
                    <div key={i} className="h-16 bg-gray-100 rounded-xl animate-pulse" />
                  ))}
                </div>
              ) : dayTasks.length === 0 ? (
                <div className="text-center py-12 text-gray-400">
                  <p className="text-4xl mb-3">📚</p>
                  <p className="font-medium">今日暂无任务</p>
                  <p className="text-sm mt-1">点击"添加任务"开始今天的复习！</p>
                </div>
              ) : (
                <div className="space-y-3">
                  {SUBJECTS.filter((s) => dayTasks.some((t) => t.subject === s)).map((subject) => {
                    const cfg = SUBJECT_CONFIG[subject];
                    const subTasks = dayTasks.filter((t) => t.subject === subject);
                    return (
                      <div key={subject}>
                        <div
                          className={`flex items-center gap-1.5 mb-2 text-xs font-semibold ${cfg.color}`}
                        >
                          <span>{cfg.icon}</span>
                          <span>{subject}</span>
                          <span className="text-gray-300">({subTasks.length})</span>
                        </div>
                        <div className="space-y-2 pl-1">
                          {subTasks.map((task) => (
                            <TaskCard
                              key={task.id}
                              task={task}
                              onToggle={handleToggle}
                              onDelete={handleDelete}
                            />
                          ))}
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </CardContent>
          </Card>
        )}

        {/* ── WEEK VIEW ── */}
        {viewMode === "week" && (
          <div className="space-y-3">
            {weekDates.map((d) => {
              const dateTasks = tasksByDate[d] || [];
              const isToday = d === todayString();
              const completedCount = dateTasks.filter((t) => t.is_completed).length;

              return (
                <Card
                  key={d}
                  className={`shadow-sm border transition-all ${
                    isToday ? "border-blue-400 ring-2 ring-blue-200" : "border-gray-200"
                  }`}
                >
                  <CardHeader className="py-3 px-4 border-b">
                    <div className="flex items-center justify-between">
                      <CardTitle className="text-sm font-semibold text-gray-700 flex items-center gap-2">
                        {isToday && (
                          <span className="px-1.5 py-0.5 bg-blue-500 text-white text-xs rounded-md">
                            今天
                          </span>
                        )}
                        {format(new Date(d + "T00:00:00"), "M月d日 (EEE)", { locale: zhCN })}
                      </CardTitle>
                      {dateTasks.length > 0 && (
                        <span className="text-xs text-gray-400">
                          {completedCount}/{dateTasks.length} 已完成
                        </span>
                      )}
                    </div>
                  </CardHeader>
                  <CardContent className="pt-3 pb-3 px-4">
                    {loading ? (
                      <div className="h-10 bg-gray-100 rounded-lg animate-pulse" />
                    ) : dateTasks.length === 0 ? (
                      <p className="text-xs text-gray-300 py-1">暂无任务</p>
                    ) : (
                      <div className="space-y-2">
                        {dateTasks.map((task) => (
                          <TaskCard
                            key={task.id}
                            task={task}
                            onToggle={handleToggle}
                            onDelete={handleDelete}
                          />
                        ))}
                      </div>
                    )}
                  </CardContent>
                </Card>
              );
            })}
          </div>
        )}
      </main>
    </div>
  );
}
