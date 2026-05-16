# 📚 PSLE 复习计划 | PSLE Revision Planner

一个为新加坡小六会考 (PSLE) 量身定制的复习计划管理网站。

## ✨ 功能特性

| 功能 | 描述 |
|------|------|
| 📅 日/周视图 | 按天或按周查看学习任务 |
| ✅ 状态追踪 | 一键切换任务完成状态 |
| 📊 进度仪表盘 | 实时显示今日/本周完成百分比 |
| 🔒 极简登录 | 全局密码保护，无需注册账号 |
| 📱 移动优先 | 响应式设计，手机和电脑均可使用 |
| 🗂️ 四大科目 | English · 数学 · 华文 · Science |

---

## 🚀 快速开始

### 1. 前置要求

- [Node.js](https://nodejs.org/) ≥ 18
- [Supabase](https://supabase.com/) 账号（免费层即可）
- [Vercel](https://vercel.com/) 账号（用于部署）

### 2. 克隆并安装依赖

```bash
cd psle-planner
npm install
```

### 3. 配置 Supabase

#### a. 创建数据库表

登录 [Supabase Dashboard](https://supabase.com/dashboard) → 选择你的项目 → **SQL Editor** → 粘贴并运行 `sql/setup.sql` 中的内容。

#### b. 获取 API Keys

在 Supabase Dashboard → **Project Settings** → **API** 中找到：

- **Project URL** → `NEXT_PUBLIC_SUPABASE_URL`
- **anon public key** → `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- **service_role secret key** → `SUPABASE_SERVICE_ROLE_KEY`

### 4. 配置环境变量

```bash
cp .env.local.example .env.local
```

编辑 `.env.local`，填入你的值：

```env
NEXT_PUBLIC_SUPABASE_URL=https://xxxxxxxxxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbG...
SUPABASE_SERVICE_ROLE_KEY=eyJhbG...

# 自定义登录密码
APP_PASSWORD=my_family_password_2024

# 随机字符串（用于签名 Cookie）
SESSION_SECRET=at_least_32_random_characters_here
```

### 5. 启动开发服务器

```bash
npm run dev
```

打开 [http://localhost:3000](http://localhost:3000)，使用你设置的 `APP_PASSWORD` 登录。

---

## 🌐 部署到 Vercel

### 方式一：GitHub + Vercel（推荐）

1. 将代码推送到 GitHub 仓库
2. 在 [Vercel Dashboard](https://vercel.com/dashboard) 点击 **"New Project"**
3. 导入你的 GitHub 仓库
4. 在 **Environment Variables** 中添加以下变量：

| Variable | Description |
|----------|-------------|
| `NEXT_PUBLIC_SUPABASE_URL` | Supabase 项目 URL |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Supabase 匿名公钥 |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase 服务角色私钥 |
| `APP_PASSWORD` | 登录密码 |
| `SESSION_SECRET` | Cookie 签名密钥（≥32位随机字符串） |

5. 点击 **"Deploy"** — 完成！

### 方式二：Vercel CLI

```bash
npm i -g vercel
vercel
# 按提示操作，然后在 Vercel Dashboard 中设置环境变量
```

---

## 📁 项目结构

```
psle-planner/
├── app/
│   ├── layout.tsx              # 根布局
│   ├── page.tsx                # 登录页
│   ├── dashboard/
│   │   └── page.tsx            # 主仪表盘（受保护）
│   └── api/
│       ├── auth/
│       │   ├── login/route.ts  # 登录 API
│       │   └── logout/route.ts # 登出 API
│       └── tasks/
│           ├── route.ts        # GET（列表）/ POST（创建）
│           └── [id]/route.ts   # PATCH（更新）/ DELETE（删除）
├── components/
│   ├── ui/                     # Shadcn UI 基础组件
│   ├── TaskCard.tsx            # 任务卡片
│   ├── AddTaskDialog.tsx       # 添加任务弹窗
│   └── ProgressDashboard.tsx   # 进度仪表盘
├── lib/
│   ├── supabase.ts             # 客户端 Supabase
│   ├── supabase-server.ts      # 服务端 Supabase
│   └── utils.ts                # 工具函数 + 常量
├── middleware.ts               # 路由保护
├── sql/
│   └── setup.sql               # 数据库建表 SQL
└── .env.local.example          # 环境变量模板
```

---

## 🗄️ 数据库结构

```sql
tasks
├── id           UUID (主键, 自动生成)
├── date         DATE (学习日期, YYYY-MM-DD)
├── subject      TEXT (English | Math | Chinese | Science)
├── content      TEXT (任务内容描述)
├── is_completed BOOLEAN (是否完成, 默认 false)
└── created_at   TIMESTAMPTZ (创建时间, 自动生成)
```

---

## 🔐 安全说明

- 登录密码存储在环境变量 `APP_PASSWORD` 中，**不存储在数据库**
- 登录成功后设置 `httpOnly` Cookie，防止 XSS 攻击
- Middleware 保护所有 `/dashboard` 和 `/api/tasks` 路由
- 数据库操作使用 Service Role Key（仅在服务器端使用）

---

## 🛠️ 技术栈

- **Framework**: Next.js 14 (App Router)
- **Styling**: Tailwind CSS + Shadcn UI
- **Database**: Supabase (PostgreSQL)
- **Deployment**: Vercel
- **Date utilities**: date-fns
- **UI Primitives**: Radix UI
