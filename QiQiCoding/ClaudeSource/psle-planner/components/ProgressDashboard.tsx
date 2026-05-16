"use client";

import { Task } from "@/lib/supabase";
import { SUBJECT_CONFIG, SUBJECTS } from "@/lib/utils";
import { Progress } from "@/components/ui/progress";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { CheckCircle2, Circle, TrendingUp } from "lucide-react";

interface ProgressDashboardProps {
  tasks: Task[];
  label?: string; // e.g. "今日" or "本周"
}

export function ProgressDashboard({ tasks, label = "今日" }: ProgressDashboardProps) {
  const total = tasks.length;
  const completed = tasks.filter((t) => t.is_completed).length;
  const percent = total === 0 ? 0 : Math.round((completed / total) * 100);

  // Per-subject stats
  const subjectStats = SUBJECTS.map((s) => {
    const subjectTasks = tasks.filter((t) => t.subject === s);
    const done = subjectTasks.filter((t) => t.is_completed).length;
    const pct = subjectTasks.length === 0 ? 0 : Math.round((done / subjectTasks.length) * 100);
    return { subject: s, total: subjectTasks.length, done, pct };
  }).filter((s) => s.total > 0);

  if (total === 0) {
    return (
      <Card className="border-2 border-dashed border-gray-200 bg-gray-50/50">
        <CardContent className="flex flex-col items-center justify-center py-8 text-center">
          <Circle className="w-10 h-10 text-gray-300 mb-2" />
          <p className="text-gray-400 text-sm">{label}暂无学习任务</p>
          <p className="text-gray-300 text-xs mt-1">点击"添加任务"开始规划吧！</p>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="border-0 shadow-lg bg-gradient-to-br from-blue-600 to-indigo-600 text-white">
      <CardHeader className="pb-3">
        <CardTitle className="text-lg flex items-center gap-2 text-white">
          <TrendingUp className="w-5 h-5" />
          {label}进度
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* Overall */}
        <div>
          <div className="flex items-center justify-between mb-2">
            <div className="flex items-center gap-2">
              <CheckCircle2 className="w-4 h-4 text-blue-200" />
              <span className="text-sm text-blue-100">
                已完成 {completed} / {total} 项
              </span>
            </div>
            <span className="text-3xl font-bold tabular-nums">{percent}%</span>
          </div>
          <Progress
            value={percent}
            className="h-3 bg-blue-500/40 [&>div]:bg-white [&>div]:transition-all [&>div]:duration-500"
          />
        </div>

        {/* Per-subject breakdown */}
        {subjectStats.length > 0 && (
          <div className="grid grid-cols-2 gap-2 pt-1">
            {subjectStats.map(({ subject, total: t, done, pct }) => {
              const cfg = SUBJECT_CONFIG[subject];
              return (
                <div key={subject} className="bg-white/15 rounded-xl p-2.5 backdrop-blur-sm">
                  <div className="flex items-center gap-1.5 mb-1.5">
                    <span className="text-base">{cfg.icon}</span>
                    <span className="text-xs font-medium text-white truncate">{subject}</span>
                  </div>
                  <Progress
                    value={pct}
                    className="h-1.5 bg-white/20 [&>div]:bg-white"
                  />
                  <p className="text-xs text-blue-200 mt-1">
                    {done}/{t} · {pct}%
                  </p>
                </div>
              );
            })}
          </div>
        )}
      </CardContent>
    </Card>
  );
}
