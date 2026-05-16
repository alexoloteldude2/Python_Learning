"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { BookOpen, Lock } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";

export default function LoginPage() {
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const router = useRouter();

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password }),
      });

      if (res.ok) {
        router.push("/dashboard");
      } else {
        const data = await res.json();
        setError(data.error || "密码错误，请重试。");
      }
    } catch {
      setError("网络错误，请稍后重试。");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        {/* Logo area */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-blue-600 mb-4 shadow-lg">
            <BookOpen className="w-8 h-8 text-white" />
          </div>
          <h1 className="text-3xl font-bold text-gray-900">PSLE 复习计划</h1>
          <p className="text-gray-500 mt-1 text-sm">Primary School Leaving Examination Planner</p>
        </div>

        <Card className="shadow-xl border-0 bg-white/80 backdrop-blur-sm">
          <CardHeader className="text-center pb-2">
            <CardTitle className="text-xl flex items-center justify-center gap-2">
              <Lock className="w-5 h-5 text-blue-600" />
              进入计划系统
            </CardTitle>
            <CardDescription>请输入访问密码以继续</CardDescription>
          </CardHeader>
          <CardContent className="pt-4">
            <form onSubmit={handleLogin} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="password">访问密码</Label>
                <Input
                  id="password"
                  type="password"
                  placeholder="请输入密码..."
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="text-center text-lg tracking-widest h-12"
                  autoFocus
                />
              </div>

              {error && (
                <div className="text-sm text-red-500 bg-red-50 border border-red-200 rounded-lg px-3 py-2 text-center">
                  {error}
                </div>
              )}

              <Button
                type="submit"
                className="w-full h-12 text-base font-semibold bg-blue-600 hover:bg-blue-700"
                disabled={loading || !password}
              >
                {loading ? "验证中..." : "进入 →"}
              </Button>
            </form>
          </CardContent>
        </Card>

        {/* Subject tags */}
        <div className="flex justify-center gap-2 mt-6 flex-wrap">
          {[
            { name: "English", color: "bg-emerald-100 text-emerald-700" },
            { name: "数学", color: "bg-blue-100 text-blue-700" },
            { name: "华文", color: "bg-red-100 text-red-700" },
            { name: "Science", color: "bg-amber-100 text-amber-700" },
          ].map((s) => (
            <span key={s.name} className={`px-3 py-1 rounded-full text-xs font-medium ${s.color}`}>
              {s.name}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}
