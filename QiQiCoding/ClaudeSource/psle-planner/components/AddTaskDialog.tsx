"use client";

import { useState } from "react";
import { format } from "date-fns";
import { CalendarIcon, Plus } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { Calendar } from "@/components/ui/calendar";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import { SUBJECTS, SUBJECT_CONFIG } from "@/lib/utils";
import { Task } from "@/lib/supabase";
import { cn } from "@/lib/utils";

interface AddTaskDialogProps {
  defaultDate?: string; // YYYY-MM-DD
  onTaskAdded: (task: Task) => void;
}

export function AddTaskDialog({ defaultDate, onTaskAdded }: AddTaskDialogProps) {
  const [open, setOpen] = useState(false);
  const [date, setDate] = useState<Date | undefined>(
    defaultDate ? new Date(defaultDate + "T00:00:00") : new Date()
  );
  const [subject, setSubject] = useState<string>("");
  const [content, setContent] = useState("");
  const [calOpen, setCalOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!date || !subject || !content.trim()) return;
    setLoading(true);
    setError("");

    const dateStr = format(date, "yyyy-MM-dd");

    try {
      const res = await fetch("/api/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ date: dateStr, subject, content: content.trim() }),
      });

      if (!res.ok) {
        const data = await res.json();
        setError(data.error || "创建任务失败，请重试。");
        return;
      }

      const newTask: Task = await res.json();
      onTaskAdded(newTask);
      setContent("");
      setSubject("");
      setOpen(false);
    } catch {
      setError("网络错误，请稍后重试。");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button className="gap-2 bg-blue-600 hover:bg-blue-700 shadow-md">
          <Plus className="h-4 w-4" />
          添加任务
        </Button>
      </DialogTrigger>

      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle className="text-xl">📝 新增学习任务</DialogTitle>
        </DialogHeader>

        <form onSubmit={handleSubmit} className="space-y-5 pt-2">
          {/* Date picker */}
          <div className="space-y-2">
            <Label>学习日期</Label>
            <Popover open={calOpen} onOpenChange={setCalOpen}>
              <PopoverTrigger asChild>
                <Button
                  variant="outline"
                  className={cn(
                    "w-full justify-start text-left font-normal h-10",
                    !date && "text-muted-foreground"
                  )}
                >
                  <CalendarIcon className="mr-2 h-4 w-4 text-blue-500" />
                  {date ? format(date, "yyyy年M月d日 (EEEE)", { locale: undefined }) : "选择日期"}
                </Button>
              </PopoverTrigger>
              <PopoverContent className="w-auto p-0" align="start">
                <Calendar
                  mode="single"
                  selected={date}
                  onSelect={(d) => {
                    setDate(d);
                    setCalOpen(false);
                  }}
                  initialFocus
                />
              </PopoverContent>
            </Popover>
          </div>

          {/* Subject selector */}
          <div className="space-y-2">
            <Label>科目</Label>
            <Select value={subject} onValueChange={setSubject}>
              <SelectTrigger className="h-10">
                <SelectValue placeholder="选择科目..." />
              </SelectTrigger>
              <SelectContent>
                {SUBJECTS.map((s) => {
                  const cfg = SUBJECT_CONFIG[s];
                  return (
                    <SelectItem key={s} value={s}>
                      <span className="flex items-center gap-2">
                        <span>{cfg.icon}</span>
                        <span>{cfg.label}</span>
                      </span>
                    </SelectItem>
                  );
                })}
              </SelectContent>
            </Select>
          </div>

          {/* Content */}
          <div className="space-y-2">
            <Label>任务内容</Label>
            <Textarea
              placeholder="例如：完成数学练习册 P.45-50，复习分数章节..."
              value={content}
              onChange={(e) => setContent(e.target.value)}
              className="min-h-[100px] text-sm"
            />
          </div>

          {error && (
            <p className="text-sm text-red-500 bg-red-50 rounded-lg px-3 py-2">{error}</p>
          )}

          <DialogFooter className="gap-2">
            <Button type="button" variant="outline" onClick={() => setOpen(false)}>
              取消
            </Button>
            <Button
              type="submit"
              disabled={loading || !date || !subject || !content.trim()}
              className="bg-blue-600 hover:bg-blue-700"
            >
              {loading ? "添加中..." : "确认添加 ✓"}
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}
