---
id: 039
title: Textbook Platform Architectural Plan
stage: plan
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: 002-textbook-platform
branch: 002-textbook-platform
user: SHAZ
command: /sp.plan
labels: ["architecture", "planning", "RAG", "Next.js", "FastAPI", "Chroma"]
links:
  spec: specs/002-textbook-platform/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/002-textbook-platform/plan.md
  - specs/002-textbook-platform/research.md
  - specs/002-textbook-platform/data-model.md
  - specs/002-textbook-platform/quickstart.md
  - specs/002-textbook-platform/contracts/api.yaml
tests:
  - none
---

## Prompt

```
/sp.plan
```

## Response snapshot

Successfully completed architectural planning for AI-Native Physical AI & Humanoid Robotics Textbook Platform.

**Phase 0: Research (Completed)**
- Launched 6 parallel research agents for technology evaluation
- Evaluated frontend frameworks (Next.js, Docusaurus, React+Vite)
- Evaluated backend frameworks (FastAPI existing, confirmed)
- Evaluated vector databases (Chroma selected over Pinecone, Weaviate, FAISS)
- Evaluated databases (PostgreSQL selected, upgrade from SQLite)
- Researched RTL layout best practices for Urdu translation
- Researched RAG with conversation history patterns
- Consolidated findings in `research.md` with detailed rationales

**Key Technology Decisions**:
1. **Frontend**: Next.js 15 (App Router + Static Export)
   - Rationale: Balance between docs features and app customization
   - Alternatives rejected: Docusaurus (limited customization), Vite SPA (no SSG)

2. **Backend**: FastAPI (existing, keep and enhance)
   - Already in place with RAG capabilities
   - Add: Auth, translation, quiz, dashboard APIs

3. **Vector Database**: Chroma (embedded mode)
   - Rationale: Zero cost, simple setup, perfect for 10K chunks
   - Alternatives rejected: Pinecone ($70/month), Weaviate (Docker overhead)

4. **Database**: PostgreSQL (upgrade from SQLite)
   - Rationale: ACID transactions, JSON support, free tier (Railway 512MB)
   - Migration path defined with Alembic

5. **Authentication**: NextAuth.js (frontend) + JWT (backend)
   - HTTP-only cookies, bcrypt password hashing

6. **Deployment**: Vercel (frontend) + Railway (backend)
   - Free tiers sufficient for hackathon/demo

**Phase 1: Design & Contracts (Completed)**
- Designed 9 database entities with relationships and indexes
  - User, UserPreferences, Chapter, ReadingProgress
  - ChatMessage, ChatCitation, Quiz, QuizAttempt, TranslationCache
- Created comprehensive OpenAPI 3.0 specification
  - 20+ endpoints across 7 resource groups
  - Full request/response schemas
  - JWT authentication security scheme
- Defined JSON schemas for quiz questions and conversation context
- Specified performance indexes for dashboard queries

**Phase 2: Quickstart & Plan (Completed)**
- Generated quickstart.md with setup instructions
  - Backend: PostgreSQL, Chroma, OpenAI integration
  - Frontend: Next.js, MDX, Tailwind, NextAuth
  - Implementation patterns for RAG, RTL, progress tracking
  - Deployment guides for Railway and Vercel
- Updated plan.md with complete architecture
  - Technical context and dependencies
  - Project structure (frontend/ + backend/)
  - Implementation workflow (P1-P4 priorities)
  - Key technical challenges and solutions
  - Testing strategy, deployment architecture
  - Security measures, cost estimates

**Artifacts Created**:
1. `research.md` (150+ lines) - Technology decisions with rationales
2. `data-model.md` (450+ lines) - Complete database schema
3. `contracts/api.yaml` (550+ lines) - OpenAPI specification
4. `quickstart.md` (300+ lines) - Developer setup guide
5. `plan.md` (500+ lines) - Implementation plan

**Architecture Highlights**:
- Monorepo structure (frontend/ + backend/)
- FastAPI backend extends existing RAG chatbot
- Next.js frontend with MDX chapter rendering
- Chroma vector DB for RAG (10K textbook chunks)
- PostgreSQL for user data, progress, chat history
- Multi-turn conversation (last 3 exchanges context)
- RTL layout toggle for Urdu translation
- Translation caching to reduce API costs
- Real-time progress tracking via HTTP polling
- Quiz generation with immediate AI feedback

**Next Steps**: Run `/sp.tasks` to generate detailed task breakdown for implementation.

## Outcome

- ✅ Impact: Complete architectural plan with 5 design artifacts covering technology selection, data models, API contracts, setup guide, and implementation roadmap. Ready for task generation and development.
- 🧪 Tests: No automated tests (planning phase)
- 📁 Files: Created 5 artifacts totaling ~2000 lines of planning documentation
- 🔁 Next prompts: Run `/sp.tasks` to generate dependency-ordered tasks for implementation
- 🧠 Reflection: Successfully decomposed complex multi-feature platform into concrete technical decisions. Research agents provided valuable input on framework trade-offs. Architecture balances feature richness (8 user stories) with implementation feasibility (existing backend, free-tier deployments).

## Evaluation notes (flywheel)

- Failure modes observed: Some research agents timeout waiting for completion; mitigated by reading available outputs and making informed decisions based on existing backend code
- Graders run and results (PASS/FAIL): Planning checklist PASS (all phases completed, no technical unknowns remaining)
- Prompt variant (if applicable): Standard /sp.plan workflow with parallel research agents
- Next experiment (smallest change to try): Consider shorter research prompts to reduce agent execution time while maintaining quality of recommendations
