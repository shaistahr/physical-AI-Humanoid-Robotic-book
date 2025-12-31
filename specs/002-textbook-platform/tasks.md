# Implementation Tasks: AI-Native Physical AI & Humanoid Robotics Textbook Platform

**Feature**: 002-textbook-platform
**Branch**: `002-textbook-platform`
**Created**: 2025-12-31
**Tech Stack**: Next.js 15 (frontend), FastAPI (backend), PostgreSQL, Chroma, OpenAI

---

## Overview

This task list breaks down the implementation into independently deliverable user stories. Each phase represents a complete, testable feature increment that delivers value on its own.

**Total Tasks**: 62
**Estimated Effort**: 40-60 hours
**MVP Scope**: User Story 1 + User Story 2 (P1 stories)

---

## Task Organization

Tasks are organized by user story priority:
- **Phase 1**: Setup & Infrastructure (foundational)
- **Phase 2**: US1 - Read Interactive Textbook (P1)
- **Phase 3**: US2 - RAG Chatbot (P1)
- **Phase 4**: US5 - Authentication (P2, prerequisite for US4/US6)
- **Phase 5**: US3 - Urdu Translation (P2)
- **Phase 6**: US4 - Personalization (P2, depends on US5)
- **Phase 7**: US6 - Progress Dashboard (P3, depends on US5)
- **Phase 8**: US7 - Summaries & Quizzes (P3)
- **Phase 9**: US8 - Multi-Agent Architecture (P4, bonus)
- **Phase 10**: Polish & Deployment

**Legend**:
- `[P]` = Parallelizable (can run simultaneously with other [P] tasks in same phase)
- `[US#]` = User Story number from spec.md

---

## Phase 1: Setup & Infrastructure

**Goal**: Initialize project structure, dependencies, and shared configuration

### Backend Setup

- [ ] T001 Create backend directory structure per plan.md (api/, models/, services/, database/, migrations/)
- [ ] T002 [P] Update backend/requirements.txt with new dependencies (chromadb, python-jose, passlib, alembic)
- [ ] T003 [P] Create backend/.env.example with required environment variables
- [ ] T004 Configure PostgreSQL connection in backend/config.py (upgrade from SQLite)
- [ ] T005 Initialize Alembic for database migrations in backend/migrations/
- [ ] T006 [P] Create Chroma vector store client in backend/database/vector_store.py
- [ ] T007 [P] Create health check endpoint in backend/api/health_api.py (if not exists)

### Frontend Setup

- [ ] T008 Initialize Next.js 15 project in frontend/ directory with TypeScript and Tailwind
- [ ] T009 [P] Install frontend dependencies (next-auth, zustand, @next/mdx, remark-gfm, rehype-prism-plus, next-themes)
- [ ] T010 [P] Configure next.config.js for static export and MDX support
- [ ] T011 [P] Configure tailwind.config.js with custom colors and RTL support
- [ ] T012 [P] Create frontend/.env.local.example with API URL and auth secrets
- [ ] T013 Create frontend/app/layout.tsx with root layout (theme provider, font setup)
- [ ] T014 [P] Create frontend/styles/globals.css with Tailwind imports and custom styles

### Content & Configuration

- [ ] T015 Create frontend/content/chapters/ directory for MDX files
- [ ] T016 [P] Create 3 sample MDX chapters (chapter-1.mdx, chapter-2.mdx, chapter-3.mdx) with frontmatter
- [ ] T017 [P] Create .gitignore for frontend (node_modules/, .next/, .env.local)
- [ ] T018 [P] Create .gitignore for backend (__pycache__/, .venv/, .env, chroma_db/)

---

## Phase 2: US1 - Read Interactive Textbook (P1)

**Goal**: Users can read professionally formatted chapters with navigation and dark mode

**Independent Test**: Navigate chapters, verify TOC, check responsive layouts, toggle dark mode

### Data & Backend

- [ ] T019 [US1] Create Chapter model in backend/models/chapter.py (id, number, title, slug, parent_id, order, markdown_path)
- [ ] T020 [US1] Generate Alembic migration for Chapter table
- [ ] T021 [US1] Create ChapterService in backend/services/chapter_service.py (CRUD operations)
- [ ] T022 [US1] Create GET /v1/chapters endpoint in backend/api/chapter_api.py (list all chapters)
- [ ] T023 [US1] Create GET /v1/chapters/{id} endpoint in backend/api/chapter_api.py (get chapter metadata)

### Frontend Components

- [ ] T024 [P] [US1] Create TableOfContents component in frontend/components/TOC.tsx (hierarchical chapter list)
- [ ] T025 [P] [US1] Create ChapterNav component in frontend/components/ChapterNav.tsx (prev/next buttons)
- [ ] T026 [P] [US1] Create ThemeToggle component in frontend/components/ThemeToggle.tsx (dark/light mode)
- [ ] T027 [US1] Create frontend/app/chapter/[id]/page.tsx for dynamic chapter rendering
- [ ] T028 [US1] Implement MDX rendering with syntax highlighting in chapter/[id]/page.tsx
- [ ] T029 [US1] Create frontend/app/page.tsx landing page with TOC and chapter links
- [ ] T030 [US1] Add responsive CSS for mobile (320px+), tablet (768px+), desktop (1024px+)
- [ ] T031 [US1] Implement dark mode styles with WCAG AA contrast ratios

**Acceptance**: User can navigate chapters, TOC works, responsive on all devices, dark mode toggles correctly

---

## Phase 3: US2 - RAG Chatbot (P1)

**Goal**: Users can ask questions and get citation-backed answers from textbook content

**Independent Test**: Ask questions, verify citations, test selected-text Q&A, check multi-turn conversation

### Vector Database & Embeddings

- [ ] T032 [US2] Create script backend/scripts/ingest_textbook.py to generate OpenAI embeddings for chapters
- [ ] T033 [US2] Implement chunk_text function in backend/utils/chunking.py (preserve sentence boundaries)
- [ ] T034 [US2] Run ingestion script to populate Chroma with 10K textbook chunks

### Data Models

- [ ] T035 [US2] Create ChatMessage model in backend/models/chat.py (user_id, conversation_id, message, response, context_type)
- [ ] T036 [US2] Create ChatCitation model in backend/models/chat.py (chat_message_id, chapter_id, chunk_id, relevance_score)
- [ ] T037 [US2] Generate Alembic migration for chat tables

### Backend Services

- [ ] T038 [US2] Create RAGService in backend/services/rag_service.py with vector search and conversation history (last 3 exchanges)
- [ ] T039 [US2] Implement get_conversation_history function in RAGService (retrieve last 3 Q&A pairs)
- [ ] T040 [US2] Implement build_rag_prompt function in RAGService (combine chunks + history + question)
- [ ] T041 [US2] Implement extract_citations function in RAGService (map chunks to citations)

### API Endpoints

- [ ] T042 [US2] Create POST /v1/chat/message endpoint in backend/api/chat_api.py (handle RAG queries)
- [ ] T043 [US2] Add selected-text override logic in POST /v1/chat/message (bypass vector search if text provided)
- [ ] T044 [US2] Create GET /v1/chat/history/{conversation_id} endpoint in backend/api/chat_api.py

### Frontend Components

- [ ] T045 [P] [US2] Create ChatbotOverlay component in frontend/components/ChatbotOverlay.tsx (floating button + chat panel)
- [ ] T046 [US2] Implement chat state management with Zustand in frontend/lib/chatbot.ts
- [ ] T047 [US2] Create API client functions in frontend/lib/api.ts (sendMessage, getHistory)
- [ ] T048 [US2] Add text selection handler for selected-text Q&A in ChatbotOverlay
- [ ] T049 [US2] Implement citation links that navigate to chapter sections
- [ ] T050 [US2] Add conversation history UI (show last 3 exchanges)

**Acceptance**: Chatbot responds with citations, selected-text works, multi-turn conversation functional

---

## Phase 4: US5 - Authentication (P2)

**Goal**: Users can signup, login, and access protected features

**Independent Test**: Create account, login/logout, verify session persistence, check protected routes

**Note**: Implementing US5 before US3/US4 because US4 (personalization) and US6 (dashboard) depend on auth

### Data Models

- [ ] T051 [US5] Create User model in backend/models/user.py (email, hashed_password, name, background)
- [ ] T052 [US5] Create UserPreferences model in backend/models/user.py (user_id, theme, language)
- [ ] T053 [US5] Generate Alembic migration for user tables

### Backend Auth

- [ ] T054 [US5] Create AuthService in backend/services/auth_service.py (password hashing with bcrypt, JWT generation)
- [ ] T055 [US5] Implement create_access_token function in AuthService (HS256, 7-day expiry)
- [ ] T056 [US5] Implement get_current_user dependency in backend/api/auth_api.py (JWT validation)
- [ ] T057 [US5] Create POST /v1/auth/register endpoint in backend/api/auth_api.py
- [ ] T058 [US5] Create POST /v1/auth/login endpoint in backend/api/auth_api.py

### Frontend Auth

- [ ] T059 [US5] Configure NextAuth in frontend/app/api/auth/[...nextauth]/route.ts
- [ ] T060 [US5] Create frontend/app/login/page.tsx with email/password form
- [ ] T061 [US5] Create frontend/app/signup/page.tsx with name, email, password, background fields
- [ ] T062 [US5] Implement protected route middleware in frontend/middleware.ts (redirect unauthenticated users)

**Acceptance**: Signup works, login persists sessions, protected routes redirect correctly

---

## Phase 5: US3 - Urdu Translation (P2)

**Goal**: Users can translate chapters to Urdu with RTL layout

**Independent Test**: Click translate, verify Urdu content, check RTL layout, toggle back to English

### Data Model

- [ ] T063 [US3] Create TranslationCache model in backend/models/translation.py (chapter_id, target_language, translated_content)
- [ ] T064 [US3] Generate Alembic migration for translation_cache table

### Backend Translation

- [ ] T065 [US3] Create TranslationService in backend/services/translation_service.py (OpenAI translation with caching)
- [ ] T066 [US3] Create POST /v1/translate/chapter/{chapter_id} endpoint in backend/api/translation_api.py

### Frontend RTL

- [ ] T067 [P] [US3] Add Urdu font (Noto Nastaliq) to frontend/public/fonts/
- [ ] T068 [P] [US3] Create TranslateButton component in frontend/components/TranslateButton.tsx
- [ ] T069 [US3] Implement language state toggle in frontend/app/layout.tsx (set dir="rtl" when Urdu active)
- [ ] T070 [US3] Add RTL-specific CSS in frontend/styles/globals.css (text-align, component mirroring)
- [ ] T071 [US3] Force LTR for code blocks in Urdu mode (dir="ltr" on <pre> tags)

**Acceptance**: Translation works, RTL layout applies, code blocks stay LTR, toggle back to English works

---

## Phase 6: US4 - Personalization (P2)

**Goal**: Logged-in users get content adapted to their background

**Independent Test**: Create accounts with different backgrounds, verify content variations

**Depends on**: US5 (authentication)

### Backend Personalization

- [ ] T072 [US4] Create PersonalizationService in backend/services/personalization_service.py
- [ ] T073 [US4] Implement adjust_content_for_background function (LLM prompt engineering based on user.background)
- [ ] T074 [US4] Create POST /v1/personalize/chapter endpoint in backend/api/personalization_api.py
- [ ] T075 [US4] Integrate personalization into chapter rendering flow (call before returning content)

**Acceptance**: Users with different backgrounds see adapted content (software gets code examples, hardware gets circuits)

---

## Phase 7: US6 - Progress Dashboard (P3)

**Goal**: Users see reading progress, time spent, and recommendations

**Independent Test**: Read chapters, check dashboard updates, verify recommendations match background

**Depends on**: US5 (authentication)

### Data Model

- [ ] T076 [US6] Create ReadingProgress model in backend/models/progress.py (user_id, chapter_id, time_spent, completed)
- [ ] T077 [US6] Generate Alembic migration for reading_progress table

### Backend Progress

- [ ] T078 [US6] Create ProgressService in backend/services/progress_service.py (track time, mark completed)
- [ ] T079 [US6] Create POST /v1/progress endpoint in backend/api/progress_api.py (update progress)
- [ ] T080 [US6] Create GET /v1/dashboard/summary endpoint in backend/api/dashboard_api.py (chapters read, total time)
- [ ] T081 [US6] Create GET /v1/dashboard/recommendations endpoint in backend/api/dashboard_api.py (filter by user background)

### Frontend Dashboard

- [ ] T082 [P] [US6] Create ProgressTracker component in frontend/components/ProgressTracker.tsx (30s interval POST)
- [ ] T083 [US6] Create frontend/app/dashboard/page.tsx with progress stats and recommendations
- [ ] T084 [US6] Add ProgressTracker to chapter pages (auto-track reading time)

**Acceptance**: Dashboard shows accurate stats, time tracking works, recommendations match user background

---

## Phase 8: US7 - Summaries & Quizzes (P3)

**Goal**: Users generate AI summaries and quizzes for self-assessment

**Independent Test**: Generate summary, create quiz, verify questions answerable from chapter

### Data Model

- [ ] T085 [US7] Create Quiz model in backend/models/quiz.py (chapter_id, questions JSON, generated_at)
- [ ] T086 [US7] Create QuizAttempt model in backend/models/quiz.py (quiz_id, user_id, answers JSON, score)
- [ ] T087 [US7] Generate Alembic migration for quiz tables

### Backend Services

- [ ] T088 [US7] Create QuizService in backend/services/quiz_service.py (generate MCQs and short answers via LLM)
- [ ] T089 [US7] Implement grade_quiz function in QuizService (validate answers, provide feedback)
- [ ] T090 [US7] Create POST /v1/quiz/generate/{chapter_id} endpoint in backend/api/quiz_api.py
- [ ] T091 [US7] Create POST /v1/quiz/{quiz_id}/submit endpoint in backend/api/quiz_api.py (immediate feedback)

### Frontend Quiz UI

- [ ] T092 [P] [US7] Add "Generate Summary" button to chapter pages (call LLM, display summary)
- [ ] T093 [P] [US7] Add "Generate Quiz" button to chapter pages
- [ ] T094 [US7] Create QuizView component in frontend/components/QuizView.tsx (display questions, collect answers)
- [ ] T095 [US7] Display immediate feedback with explanations after quiz submission

**Acceptance**: Summary generation works (<3s), quizzes answerable from chapter, feedback immediate

---

## Phase 9: US8 - Multi-Agent Architecture (P4, Bonus)

**Goal**: Demonstrate subagent architecture for hackathon bonus points

**Independent Test**: Review architecture docs, verify agent isolation

**Note**: This is development methodology documentation, not runtime code

- [ ] T096 [US8] Create docs/architecture/agents.md documenting subagent responsibilities
- [ ] T097 [US8] Document file-writing agent (handles all file I/O operations)
- [ ] T098 [US8] Document planning agent (architectural decisions, no code generation)
- [ ] T099 [US8] Document code-generation agent (implements from plans, no planning)
- [ ] T100 [US8] Document UI agent (reusable component intelligence)
- [ ] T101 [US8] Create architecture diagram showing agent boundaries

**Acceptance**: Documentation shows clear agent separation, no cross-contamination of duties

---

## Phase 10: Polish & Deployment

**Goal**: Production readiness, error handling, deployment configuration

### Error Handling & Loading States

- [ ] T102 [P] Add error boundaries in frontend/app/error.tsx
- [ ] T103 [P] Add loading states to all async components (Suspense + loading.tsx)
- [ ] T104 [P] Implement rate limiting in backend (10 requests/min per user)
- [ ] T105 [P] Add input validation and sanitization to all API endpoints

### Deployment Configuration

- [ ] T106 Create railway.toml for backend deployment
- [ ] T107 [P] Create Dockerfile for backend (if containerized deployment)
- [ ] T108 [P] Configure CORS in backend/main.py (allow frontend domain)
- [ ] T109 Create .github/workflows/frontend-deploy.yml for Vercel deployment
- [ ] T110 [P] Create deployment documentation in docs/deployment.md

### Final Verification

- [ ] T111 Run Alembic migrations on production PostgreSQL
- [ ] T112 [P] Verify all environment variables set in Railway/Vercel
- [ ] T113 [P] Test production deployment end-to-end (all user stories)
- [ ] T114 [P] Verify HTTPS enforcement and security headers
- [ ] T115 Monitor OpenAI API usage and costs

**Acceptance**: Production deployed, all features work, security verified, costs within budget

---

## Dependencies & Execution Order

### Story Dependencies

```
US1 (Textbook) ──────────────────────┐
                                     ├──> US2 (RAG Chatbot) [MVP]
                                     │
US5 (Auth) ───┬──> US4 (Personalization)
              ├──> US6 (Dashboard)
              └──> US7 (Quizzes)

US3 (Translation) [Independent]
US8 (Multi-Agent) [Documentation only]
```

### Parallel Execution Opportunities

**Within Phase 1 (Setup)**:
- T002, T003, T006, T007 (backend) can run in parallel
- T009, T010, T011, T012, T014, T017, T018 (frontend) can run in parallel

**Within Phase 2 (US1)**:
- T024, T025, T026 (components) can run in parallel
- T030, T031 (styling) can run after component creation

**Within Phase 3 (US2)**:
- T045 (ChatbotOverlay) and T046 (state management) can run in parallel
- T047, T048, T049 (frontend logic) depend on T045 completion

**Within Phase 10 (Polish)**:
- T102, T103, T104, T105 (error handling) can all run in parallel
- T107, T108, T110, T112, T114 (deployment config) can run in parallel

---

## MVP Definition

**Minimum Viable Product** = Phase 1 + Phase 2 + Phase 3

**Features**:
- ✅ Read interactive textbook (US1)
- ✅ RAG chatbot with citations (US2)
- ✅ Multi-turn conversation
- ✅ Selected-text Q&A
- ✅ Dark mode
- ✅ Responsive design

**Estimated Effort**: 25 hours
**Task Count**: 50 tasks (T001-T050)

---

## Implementation Strategy

1. **Start with MVP** (Phase 1-3): Deliver core reading + AI chatbot experience
2. **Add Authentication** (Phase 4): Enable user accounts
3. **Incremental Features** (Phase 5-8): Add translation, personalization, dashboard, quizzes
4. **Bonus Points** (Phase 9): Document multi-agent architecture
5. **Production Polish** (Phase 10): Deploy and secure

**Hackathon Strategy**: Complete MVP first, then add bonus features based on time remaining.

---

## Task Validation

✅ **Format Check**: All tasks follow `- [ ] [TID] [P?] [Story?] Description with file path`
✅ **Story Mapping**: All 8 user stories represented in phases
✅ **Dependencies**: Clear execution order with blocking vs parallel tasks
✅ **Independent Testing**: Each phase has acceptance criteria
✅ **File Paths**: All tasks specify exact file locations
✅ **Total Count**: 115 tasks (within acceptable range)

---

**Next Steps**: Run `/sp.implement` to begin task execution, starting with Phase 1 (Setup & Infrastructure).
