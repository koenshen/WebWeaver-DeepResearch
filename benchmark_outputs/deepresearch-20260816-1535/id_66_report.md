
# Obsidian Plugins for Notion-Style Multi-View Databases: A Comprehensive Comparison

## 1. Introduction

Notion’s core appeal lies in its ability to turn any database into multiple visual perspectives — **Table**, **Kanban (Board)**, **Calendar**, **List**, **Gallery**, and more — all drawing from the same underlying data. Obsidian, being a local-first Markdown ecosystem, does not ship this functionality out of the box (except for the nascent **Bases** core plugin). However, a rich ecosystem of community plugins can approximate or even exceed Notion’s multi-view capability. This report evaluates the major plugins that can replicate Notion’s multi-view database paradigm, assessing their strengths and weaknesses for each view type.

---

## 2. Plugin-by-Plugin Analysis

### 2.1 Obsidian Bases (Core Plugin)

**Status:** Core plugin, shipped with Obsidian v1.9+ (still in beta/rapid development).  
**Views:** Table, List, Cards (grid/gallery), Map. No native Kanban or Calendar yet.  
**Source:** [Obsidian Help: Introduction to Bases](https://obsidian.md/help/bases)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Table** | Fully visual editor; no coding required. Blazing fast, even on vaults with thousands of notes. Inline editing of note properties. | Cannot query inline metadata (only YAML frontmatter properties). No grouping in views yet. |
| **List** | Clean bulleted/numbered list view. Filters and sorting apply visually. | Very basic; no rich formatting. |
| **Cards** | Grid/gallery layout with cover images. Good for visual browsing. | Limited customization of card layout. |
| **Map** | Interactive map pins from location properties. | Niche use case. |
| **Kanban** | **Not available natively** — must be added via community plugins (see below). | Will be added to official roadmap; currently absent. |
| **Calendar** | **Not available natively** — must be added via community plugins. | Planned for future releases. |

**Overall Strength:** Excellent performance, first-party support, and a visual filter/sort/group system. Extensible via community "Bases Views."  
**Overall Weakness:** Limited view types out of the box; no inline metadata support; no database relations.

---

### 2.2 Make.md

**Status:** Actively maintained, mature.  
**Views:** Table, Board (Kanban), Calendar (day/week/month), Gallery, Flow, List.  
**Source:** [Make.md Official Site](https://www.make.md/) | [Getting Started Guide](https://www.make.md/docs/Getting%20Started)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Table** | Rich Notion-like table with inline editing, formulas, rollups, and column calculations. Supports multiple property types (text, number, date, checkbox, relation, etc.). | Slight learning curve for advanced features. |
| **Board/Kanban** | True Kanban with drag-and-drop, status-based columns, customizable card display. | Not as deeply integrated with the broader Obsidian task ecosystem as the dedicated Kanban plugin. |
| **Calendar** | Full day, week, and month views. Powered by date properties. | Relatively new addition; still maturing. |
| **Gallery** | Visual card grid with images. | Less customizable than dedicated gallery solutions. |
| **Flow** | Continuous scroll view. | Unique to Make.md; niche. |
| **Relations** | Two-way database relations (Notion-like linked records). Formula support with rollups. | Relations performance can degrade with large datasets. |

**Overall Strength:** The closest all-in-one Notion replacement in Obsidian. Combines views, databases, formulas, relations, and dashboards in a single plugin.  
**Overall Weakness:** Can feel heavy; some users report bloat; relies on its own "Spaces" navigation paradigm which may conflict with Obsidian defaults.

---

### 2.3 Power Bases

**Status:** Actively maintained (v1.33.18+).  
**Views:** Board (Kanban), Calendar (month/week), Timeline (Gantt), Chart (bar/line/donut), Gallery, Advanced Table.  
**Source:** [Obsidian Community Plugins: Power Bases](https://community.obsidian.md/plugins/powerbases) | [Obsidian Stats: Power Bases](https://www.obsidianstats.com/tags/bases)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Board (Kanban)** | Drag-and-drop, swimlanes, WIP limits, bulk actions. Cards update frontmatter on move. | Requires Obsidian Bases core plugin to be enabled. |
| **Calendar** | Month and week views. Drag-and-drop rescheduling writes back to notes. | Less polished than dedicated calendar plugins. |
| **Timeline (Gantt)** | Gantt-style bars with date properties. | Not as full-featured as dedicated Gantt plugins. |
| **Chart** | Bar, line, donut charts rendered as SVG from grouped data. | Basic visualization; no interactive drill-down. |
| **Gallery** | Image grid from note attachments/frontmatter. | Simple grid; limited customization. |
| **Advanced Table** | Rollups, summaries, inline editing, field types, colors, CSV import. | Can be slower with very large datasets. |

**Overall Strength:** Extends Bases with the most comprehensive set of additional views (6 extra). Portable data (plain Markdown + frontmatter).  
**Overall Weakness:** Still relatively new; some features are premium/licensed. Requires Bases.

---

### 2.4 Obsidian Projects (Discontinued)

**Status:** **Discontinued** (May 2025). Removed from community plugin listing. Can still be installed via BRAT.  
**Views:** Table, Board (Kanban), Calendar, Gallery.  
**Source:** [GitHub: obsidian-projects](https://github.com/marcusolsson/obsidian-projects)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Table** | Clean, sortable table with inline editing. | No longer maintained. |
| **Board (Kanban)** | Status-based columns; drag-and-drop. | Will not receive updates. |
| **Calendar** | Date-based views. | Unmaintained — may break with future Obsidian updates. |
| **Gallery** | Card grid view. | Defunct. |

**Overall Strength:** Was the gold standard for multi-view Notion-like databases in Obsidian.  
**Overall Weakness:** **Discontinued and effectively dead.** Not recommended for new setups.

---

### 2.5 DB Folder

**Status:** Actively maintained (by RafaelGB).  
**Views:** **Table only.**  
**Source:** [DB Folder Documentation](https://rafaelgb.github.io/obsidian-db-folder) | [GitHub](https://github.com/RafaelGB/obsidian-db-folder)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Table** | Notion-like table with inline editing, multi-column sorting, filtering, search. Uses Dataview engine for queries. Multiple sources: folder, tags, links, Dataview queries. | **No Kanban, Calendar, List, or Gallery views.** Only table. |
| **Inline metadata** | Can read inline fields (Dataview-style), not just YAML frontmatter. | Requires Dataview to be installed. |

**Overall Strength:** Excellent table implementation with powerful source flexibility.  
**Overall Weakness:** Single-view only; no multi-view paradigm.

---

### 2.6 DataLoom

**Status:** **Unmaintained** (since May 2024). Users advised to export data.  
**Views:** **Table only.**  
**Source:** [GitHub: DataLoom](https://github.com/decaf-dev/obsidian-dataloom) | [Unmaintained notice](https://github.com/decaf-dev/obsidian-dataloom/issues/958)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Table** | Rich cell types (text, number, currency, checkbox, embed, file, date, tag, multi-tag, etc.). CSV/Markdown import/export. | **Unmaintained.** Data stored in proprietary `.loom` JSON format — not plain Markdown. |

**Overall Strength:** Was the most feature-rich Notion table clone.  
**Overall Weakness:** **Dead project.** Data portability concerns. Not recommended.

---

### 2.7 Kanban Plugin (mgmeyers)

**Status:** Actively maintained, seeking new maintainers.  
**Views:** **Kanban only** (with optional Table and List display modes within the board).  
**Source:** [Obsidian Kanban Plugin Docs](https://publish.obsidian.md/kanban/) | [GitHub](https://github.com/mgmeyers/obsidian-kanban)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Kanban Board** | Excellent drag-and-drop. Card archiving, date support, checkbox tasks, images, links. Markdown data format. | Dedicated Kanban only — not a general database. Cannot easily switch to other views of the same data. |
| **Table/List within board** | Alternate view modes for the same board data. | Very basic; limited column control. |
| **Integration** | Can copy cards to Full Calendar plugin. | Lacks native calendar view. |

**Overall Strength:** The most mature and polished Kanban experience in Obsidian.  
**Overall Weakness:** Single-purpose; cannot serve as a multi-view database for arbitrary notes.

---

### 2.8 Dataview

**Status:** Mature, stable, but **no longer actively developed** (stagnant).  
**Views:** Table, List, Task, Calendar (via query).  
**Source:** [Dataview Documentation](https://blacksmithgu.github.io/obsidian-dataview/) | [Obsidian Rocks comparison](https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Table** | Powerful SQL-like query language. Can query any metadata (YAML, inline, tags). | Read-only — cannot edit data directly in the view. Sluggish on large vaults. |
| **List** | Flexible list generation from any criteria. | No inline editing. |
| **Task** | Aggregates tasks from across vault. | Limited to task format. |
| **Calendar** | Date-based results view. | Very basic; no drag-and-drop. |
| **DataviewJS** | Arbitrary JavaScript for unlimited custom views. | Requires programming knowledge. |

**Overall Strength:** Unmatched query flexibility. Can serve as the engine for other plugins (DB Folder, Projects).  
**Overall Weakness:** Read-only; performance issues; no longer evolving. Not a multi-view database — it's a query language.

---

### 2.9 Task Manager Bases View

**Status:** Actively maintained.  
**Views:** Kanban (tm-kanban), Timeline/Gantt (tm-timeline), Weekly-log Calendar (tm-calendar).  
**Source:** [Obsidian Community Plugins: Task Manager Bases View](https://community.obsidian.md/plugins/task-manager-bases-view)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Kanban** | Uses Bases group-by for columns. Predefined colored columns. Done-status with archive-all. Drag-and-drop. Changelog recording. | Requires Bases. No built-in Table view (uses Bases default table). |
| **Timeline (Gantt)** | Start/end date bars. Milestones. Multi-tier headers. Property-based labels. Drag to reschedule. | No dependency arrows. |
| **Calendar** | Weekly time grid from daily notes. Time-block parsing. Overlapping blocks. Current-time indicator. | Only weekly view; no month view. |

**Overall Strength:** Task-focused extension of Bases with three valuable views. All data remains in plain Markdown.  
**Overall Weakness:** Focused on tasks; not a general-purpose database viewer.

---

### 2.10 Kanban Bases View

**Status:** Actively maintained.  
**Views:** **Kanban only** (for Bases).  
**Source:** [Obsidian Community Plugins: Kanban Bases View](https://community.obsidian.md/plugins/kanban-bases-view) | [GitHub](https://github.com/ewerx/obsidian-bases-kanban)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Kanban** | Drag-and-drop cards between columns. Column reordering. Card sorting within columns. Add new cards directly. | Kanban only. No calendar or timeline. |

**Overall Strength:** Simple, lightweight Kanban extension for Bases. Works with any Base.  
**Overall Weakness:** Single-view; no other display modes.

---

### 2.11 Kanban Action Planner

**Status:** Actively maintained.  
**Views:** Kanban (with swimlanes, scheduling calendar mode).  
**Source:** [Kanban Action Planner Docs](https://dsebastien.github.io/obsidian-kanban-action-planner) | [GitHub](https://github.com/dsebastien/obsidian-kanban-action-planner)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Kanban** | Columns from status property. Swimlanes by note type/priority. Embeddable boards in notes. | Requires Obsidian 1.12+ (Bases view API). Desktop only. |
| **Calendar mode** | Flip board to scheduling calendar (day/week/month/quarter/year). Drag cards to set dates. Natural language date input. | Not a standalone calendar; built into board view. |
| **Note types** | Different state machines per note type. | Adds complexity. |

**Overall Strength:** Advanced Kanban with integrated scheduling. Free and open-source.  
**Overall Weakness:** Desktop only; complex setup for advanced features.

---

### 2.12 Project Manager (Obsidian-PM)

**Status:** Actively maintained.  
**Views:** Table, Kanban, Gantt.  
**Source:** [Obsidian Community Plugins: Project Manager](https://community.obsidian.md/plugins/project-manager) | [GitHub](https://github.com/StepanKropachev/obsidian-pm)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Table** | Sortable, filterable, inline editing. Quick-add bar. Bulk actions. Saved filter/sort combinations. | Project-focused; not a general note database. |
| **Kanban** | Status-based columns. Cards with all task fields. | Not a standalone Kanban for arbitrary notes. |
| **Gantt** | Interactive timeline. Draggable bars, resizable edges. Dependency arrows. Zoom from day to quarter. Milestones as diamonds. | Task-centric. |

**Overall Strength:** Full project management (dependencies, time tracking, subtasks, recurring tasks). Data stored as plain Markdown.  
**Overall Weakness:** Requires the plugin's own task note format. Not a general-purpose database viewer.

---

### 2.13 Full Calendar (Remastered)

**Status:** Actively maintained (remastered fork).  
**Views:** **Calendar only** (month, week, day, list).  
**Source:** [Obsidian Community Plugins: Full Calendar Remastered](https://community.obsidian.md/plugins/full-calendar-remastered) | [GitHub](https://github.com/obsidian-community/obsidian-full-calendar)

| Feature | Strength | Weakness |
|---------|----------|----------|
| **Calendar** | Month/week/day views. Events stored as frontmatter notes. CalDAV and Google Calendar sync (read-only). ICS support. | Calendar only; no other views. |
| **Integration** | Can pull from Bases, Obsidian Tasks, frontmatter. | Cannot serve as a general database. |

**Overall Strength:** The most capable calendar plugin for Obsidian.  
**Overall Weakness:** Single-purpose; no table, kanban, or list views.

---

## 3. Comparative Summary: View Coverage

| Plugin | Table | Kanban/Board | Calendar | List | Gallery/Cards | Gantt/Timeline | Map | Chart |
|--------|:-----:|:------------:|:--------:|:----:|:-------------:|:--------------:|:---:|:----:|
| **Bases (core)** | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ |
| **Make.md** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Power Bases** | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ |
| **Projects** (discontinued) | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| **DB Folder** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **DataLoom** (unmaintained) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Kanban Plugin** | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Dataview** | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Task Manager Bases View** | ⬜ (uses Bases) | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ |
| **Kanban Bases View** | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Kanban Action Planner** | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Project Manager** | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| **Full Calendar** | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

✅ = Native / Full support  
⬜ = Available via underlying platform (e.g., Bases table)  
❌ = Not available

---

## 4. Best Solutions by Use Case

### 4.1 All-in-One Notion Replacement
**Winner: Make.md**  
- Provides Table, Board (Kanban), Calendar (day/week/month), Gallery, Flow, and List views.  
- Supports database relations, formulas, rollups, and column calculations.  
- Includes "Spaces" for dashboard-like navigation.  
- **Weakness:** Can feel heavy; some users prefer a modular approach.

### 4.2 Modular Multi-View Stack (Bases-Centric)
**Recommended Setup: Obsidian Bases (core) + Power Bases + Task Manager Bases View (optional)**  
- Bases provides the foundation (Table, List, Cards, Map).  
- Power Bases adds Board (Kanban), Calendar, Timeline (Gantt), Chart, Gallery, and Advanced Table.  
- Task Manager Bases View adds a Kanban with changelog and a weekly calendar log.  
- **Strength:** All data stays in plain Markdown; fully modular; you only enable what you need.  
- **Weakness:** Requires multiple plugins; some Power Bases features are premium.

### 4.3 Lightweight Multi-View (Minimal Plugins)
**Recommended Setup: Obsidian Bases (core) + Kanban Bases View + Full Calendar**  
- Bases for Table/List/Cards.  
- Kanban Bases View for Kanban on any Base.  
- Full Calendar for event calendar (with possible integration).  
- **Strength:** Minimal plugin count; each plugin does one thing well.  
- **Weakness:** No single-pane-of-glass multi-view switching; views are separate.

### 4.4 Best for Project Management
**Winner: Project Manager (Obsidian-PM)**  
- Table, Kanban, and Gantt views with full project management features (dependencies, time tracking, subtasks, milestones).  
- **Alternatively:** Make.md for lighter project tracking with database relations.

### 4.5 Best for Power Querying
**Winner: Dataview** (complementary to Bases)  
- Use Dataview for complex queries, aggregations, and read-only reports.  
- Use Bases for interactive, editable views of the same data.  
- **Warning:** Dataview is no longer evolving; Datacore may eventually replace it.

---

## 5. Key Considerations and Trade-offs

### 5.1 Data Portability
- **Plain Markdown + Frontmatter:** Bases, Make.md, Power Bases, DB Folder, Kanban Bases View, Task Manager Bases View, Kanban Action Planner, Project Manager — all store data as standard Markdown files with YAML frontmatter. Your data is never locked in.  
- **Proprietary Format:** DataLoom (`.loom` JSON files) — **avoid**.  
- **Plugin-Specific Markdown:** The Kanban Plugin (mgmeyers) uses a specific Markdown format for boards; it's readable but not standard.

### 5.2 Performance
- **Bases** (core) is the fastest option, designed and optimized by the Obsidian team.  
- **Power Bases** and **Make.md** perform well but may lag with very large datasets (10,000+ notes).  
- **Dataview** is the slowest, especially on mobile and large vaults.  
- **DB Folder** depends on Dataview engine, inheriting its performance characteristics.

### 5.3 Maintenance and Longevity
- **Actively maintained:** Make.md, Power Bases, DB Folder, Task Manager Bases View, Kanban Bases View, Kanban Action Planner, Project Manager, Full Calendar (Remastered).  
- **Stagnant but stable:** Dataview.  
- **Discontinued/Dead:** Projects, DataLoom.  
- **Core (always maintained):** Bases.

### 5.4 Learning Curve
- **Lowest:** Bases (visual editor, no coding).  
- **Low:** Power Bases, DB Folder, Kanban Bases View, Full Calendar.  
- **Medium:** Make.md (many features), Kanban Action Planner (note types, state machines), Project Manager.  
- **High:** Dataview (query language), DataviewJS (JavaScript).

### 5.5 Mobile Support
- **Fully supported:** Bases, Make.md, Power Bases, DB Folder, Kanban Plugin, Full Calendar, Task Manager Bases View, Kanban Bases View, Project Manager.  
- **Desktop only:** Kanban Action Planner.

---

## 6. Conclusion

No single plugin perfectly replicates every facet of Notion's multi-view databases. However, three approaches stand out:

1. **For the closest all-in-one experience:** **Make.md** offers the most comprehensive set of views (Table, Board, Calendar, Gallery, Flow, List) with database relations, formulas, and rollups — all in a single plugin. It is the nearest equivalent to Notion's database paradigm within Obsidian.

2. **For a modular, future-proof stack:** Combine **Obsidian Bases (core)** with **Power Bases** (which adds 6 extra views including Kanban, Calendar, Gantt, and Chart) and optionally **Task Manager Bases View** for task-specific Kanban/timeline/calendar. This approach keeps your data in pure Markdown, leverages the performance of the core plugin, and allows you to add or remove views as needed.

3. **For lightweight, purpose-driven setups:** Use **Bases (core) + Kanban Bases View + Full Calendar**. Each plugin excels at its specific view type, and you avoid feature bloat.

**The golden rule:** All solutions that store data in plain Markdown with YAML frontmatter are interoperable. You can start with one approach and migrate to another without losing data. Avoid plugins that use proprietary storage formats (DataLoom) or are unmaintained (Projects, DataLoom).

---

## 7. References

1. Obsidian Help: Introduction to Bases — https://obsidian.md/help/bases
2. Make.md Official Site — https://www.make.md/
3. Make.md Getting Started Guide — https://www.make.md/docs/Getting%20Started
4. Power Bases on Obsidian Community Plugins — https://community.obsidian.md/plugins/powerbases
5. Obsidian Stats: Power Bases — https://www.obsidianstats.com/tags/bases
6. DB Folder Documentation — https://rafaelgb.github.io/obsidian-db-folder
7. DB Folder GitHub Repository — https://github.com/RafaelGB/obsidian-db-folder
8. DataLoom GitHub Repository — https://github.com/decaf-dev/obsidian-dataloom
9. DataLoom Unmaintained Notice — https://github.com/decaf-dev/obsidian-dataloom/issues/958
10. Obsidian Projects GitHub Repository — https://github.com/marcusolsson/obsidian-projects
11. Obsidian Kanban Plugin Documentation — https://publish.obsidian.md/kanban/
12. Obsidian Kanban Plugin GitHub — https://github.com/mgmeyers/obsidian-kanban
13. Dataview Documentation — https://blacksmithgu.github.io/obsidian-dataview/
14. Task Manager Bases View — https://community.obsidian.md/plugins/task-manager-bases-view
15. Kanban Bases View — https://community.obsidian.md/plugins/kanban-bases-view
16. Kanban Bases View GitHub — https://github.com/ewerx/obsidian-bases-kanban
17. Kanban Action Planner Documentation — https://dsebastien.github.io/obsidian-kanban-action-planner
18. Kanban Action Planner GitHub — https://github.com/dsebastien/obsidian-kanban-action-planner
19. Project Manager on Obsidian Community Plugins — https://community.obsidian.md/plugins/project-manager
20. Project Manager GitHub — https://github.com/StepanKropachev/obsidian-pm
21. Full Calendar Remastered — https://community.obsidian.md/plugins/full-calendar-remastered
22. Full Calendar Plugin GitHub — https://github.com/obsidian-community/obsidian-full-calendar
23. Obsidian Rocks: Dataview vs Datacore vs Obsidian Bases — https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases
24. Practical PKM: Moving to Obsidian Bases from Dataview — https://practicalpkm.com/moving-to-obsidian-bases-from-dataview
25. Reddit: Bases VS Dataview VS Make.md — https://www.reddit.com/r/ObsidianMD/comments/1n3yo5p/bases_vs_dataview_vs_makemd/
26. Obsidian Forum: What are the differences between various database plugins? — https://forum.obsidian.md/t/what-are-the-differences-between-various-database-plugins/39406
27. XDA Developers: 4 Bases plugins you should be using — https://www.xda-developers.com/bases-plugins-you-should-be-using
28. XDA Developers: I built a full Notion alternative using Obsidian plugins — https://www.xda-developers.com/build-notion-alternative-using-obsidian-plugins
29. Sébastien Dubois: How I Turned My Obsidian Notes Into Kanban Boards — https://www.dsebastien.net/how-i-turned-my-obsidian-notes-into-kanban-boards
30. Obsidian Forum: Full Calendar Remastered — https://forum.obsidian.md/t/full-calendar-remastered-the-local-first-foss-calendar-hub-caldav-google-calendar-sync-tasks-backlog-activity-tracking/114322
