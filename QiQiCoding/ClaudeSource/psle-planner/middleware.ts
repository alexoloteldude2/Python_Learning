import { NextRequest, NextResponse } from "next/server";

export function middleware(req: NextRequest) {
  const { pathname } = req.nextUrl;

  // Public routes that don't need authentication
  if (pathname === "/" || pathname.startsWith("/api/auth")) {
    return NextResponse.next();
  }

  // Check for session cookie on protected routes
  const session = req.cookies.get("psle_session");
  const isAuthenticated =
    session?.value === (process.env.SESSION_SECRET || "authenticated");

  if (!isAuthenticated) {
    return NextResponse.redirect(new URL("/", req.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/api/tasks/:path*"],
};
