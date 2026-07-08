-- Supabase SQL to ensure lotto_draws table has the required columns.
-- Run this in Supabase SQL editor for project: https://sejsqftsfutxvyzxokow.supabase.co

alter table if exists public.lotto_draws
  add column if not exists ticket_index integer,
  add column if not exists seed text,
  add column if not exists numbers integer[],
  add column if not exists formatted text,
  add column if not exists created_at timestamptz default now();

-- Enable row-level security for anonymous inserts/selects
alter table if exists public.lotto_draws enable row level security;

-- Supabase/Postgres does not support IF NOT EXISTS on CREATE POLICY.
-- Drop the policy first if it exists, then recreate.
drop policy if exists "Allow anon insert" on public.lotto_draws;
create policy "Allow anon insert" on public.lotto_draws
  for insert with check (true);

drop policy if exists "Allow anon select" on public.lotto_draws;
create policy "Allow anon select" on public.lotto_draws
  for select using (true);

-- If the table does not exist yet, use this statement instead:
-- create table public.lotto_draws (
--   id bigint generated always as identity primary key,
--   ticket_index integer,
--   seed text,
--   numbers integer[],
--   formatted text,
--   created_at timestamptz default now()
-- );
