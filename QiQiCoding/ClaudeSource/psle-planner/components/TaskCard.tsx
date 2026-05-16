"use client";

import { Task } from "@/lib/supabase";
import { SUBJECT_CONFIG } from "@/lib/utils";
import { Checkbox } from "@/components/ui/checkbox";
import { Button } from "@/components/ui/button";
import { Trash2 } from "lucide-react";
import { cn } from "@/lib/utils";

interface TaskCardProps {
  task: Task;
  onToggle: (id: string, value: boolean) => void;
  onDelete: (id: string) => void;
}

export function TaskCard({ task, onToggle, onDelete }: TaskCardProps) {
  const config = SUBJECT_CONFIG[task.subject];

  return (
    <div
      className={cn(
        "flex items-start gap-3 p-4 rounded-xl border-2 transition-all duration-200 group",
        config.bg,
        config.border,
        task.is_completed && "opacity-60"
      )}
    >
      {/* Checkbox */}
      <div className="pt-0.5 flex-shrink-0">
        <Checkbox
          checked={task.is_completed}
          onCheckedChange={(checked) => onToggle(task.id, !!checked)}
          className="h-5 w-5"
        />
      </div>

      {/* Content */}
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2 mb-1 flex-wrap">
          <span className={cn("text-xs font-semibold px-2 py-0.5 rounded-full", config.bg, config.color, "border", config.border)}>
            {config.icon} {task.subject}
          </span>
        </div>
        <p
          className={cn(
            "text-sm text-gray-800 leading-relaxed",
            task.is_completed && "line-through text-gray-400"
          )}
        >
          {task.content}
        </p>
      </div>

      {/* Delete button */}
      <Button
        variant="ghost"
        size="icon"
        className="opacity-0 group-hover:opacity-100 transition-opacity h-8 w-8 text-red-400 hover:text-red-600 hover:bg-red-50 flex-shrink-0"
        onClick={() => onDelete(task.id)}
      >
        <Trash2 className="h-4 w-4" />
      </Button>
    </div>
  );
}
