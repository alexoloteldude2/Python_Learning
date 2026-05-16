import { NextRequest, NextResponse } from "next/server";
import { createClient } from "@/lib/supabase-server";

// GET /api/tasks?date=YYYY-MM-DD  or  GET /api/tasks (all tasks)
export async function GET(req: NextRequest) {
  const supabase = createClient();
  const { searchParams } = new URL(req.url);
  const date = searchParams.get("date");
  const week = searchParams.get("week"); // YYYY-WW format week start date

  let query = supabase.from("tasks").select("*").order("created_at", { ascending: true });

  if (date) {
    query = query.eq("date", date);
  } else if (week) {
    // week = start date of week (Monday)
    const start = new Date(week);
    const end = new Date(week);
    end.setDate(end.getDate() + 6);
    query = query
      .gte("date", start.toISOString().split("T")[0])
      .lte("date", end.toISOString().split("T")[0]);
  }

  const { data, error } = await query;

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }

  return NextResponse.json(data);
}

// POST /api/tasks  → create a task
export async function POST(req: NextRequest) {
  const supabase = createClient();
  const body = await req.json();
  const { date, subject, content } = body;

  if (!date || !subject || !content) {
    return NextResponse.json({ error: "缺少必填字段: date, subject, content" }, { status: 400 });
  }

  const { data, error } = await supabase
    .from("tasks")
    .insert({ date, subject, content, is_completed: false })
    .select()
    .single();

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }

  return NextResponse.json(data, { status: 201 });
}
