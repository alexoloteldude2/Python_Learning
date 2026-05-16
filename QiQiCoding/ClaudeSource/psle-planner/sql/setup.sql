-- ============================================================
-- PSLE Revision Planner — Supabase Database Setup
-- Run this entire script in Supabase SQL Editor
-- ============================================================

-- 1. Create the tasks table
CREATE TABLE IF NOT EXISTS public.tasks (
  id            UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  date          DATE NOT NULL,
  subject       TEXT NOT NULL CHECK (subject IN ('English', 'Math', 'Chinese', 'Science')),
  content       TEXT NOT NULL,
  is_completed  BOOLEAN NOT NULL DEFAULT FALSE,
  created_at    TIMESTAMPTZ DEFAULT now() NOT NULL
);

-- 2. Index for fast date queries
CREATE INDEX IF NOT EXISTS tasks_date_idx ON public.tasks (date);

-- 3. Enable Row-Level Security (we use server-side service role key,
--    so RLS can stay simple — just block public access)
ALTER TABLE public.tasks ENABLE ROW LEVEL SECURITY;

-- 4. Policy: allow full access from service role (used by Next.js API routes)
--    If you use the anon key instead, change 'service_role' to 'anon' below.
CREATE POLICY "service_role_all" ON public.tasks
  FOR ALL
  TO service_role
  USING (true)
  WITH CHECK (true);

-- 5. (Optional) Seed some sample data to test the app
INSERT INTO public.tasks (date, subject, content, is_completed)
VALUES
  (CURRENT_DATE, 'English',  'Read comprehension passage P.12 and answer questions', false),
  (CURRENT_DATE, 'Math',     '完成练习册第 45-50 页，重点复习分数', false),
  (CURRENT_DATE, 'Chinese',  '写作文：《我最喜欢的季节》300字', false),
  (CURRENT_DATE, 'Science',  'Revise Chapter 5: Plants and their adaptations', false);
