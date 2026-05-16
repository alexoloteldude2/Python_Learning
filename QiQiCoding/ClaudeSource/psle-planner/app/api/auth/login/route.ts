import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const { password } = await req.json();
  const correctPassword = process.env.APP_PASSWORD;

  if (!correctPassword) {
    return NextResponse.json({ error: "服务器未配置密码" }, { status: 500 });
  }

  if (password !== correctPassword) {
    return NextResponse.json({ error: "密码错误，请重试。" }, { status: 401 });
  }

  const response = NextResponse.json({ success: true });
  // Set a session cookie (httpOnly, secure in production)
  response.cookies.set("psle_session", process.env.SESSION_SECRET || "authenticated", {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "lax",
    maxAge: 60 * 60 * 24 * 7, // 7 days
    path: "/",
  });

  return response;
}
