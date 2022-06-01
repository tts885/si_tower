from django.contrib import admin
from apps.commons.models import Category, Status, Stage, DelayReason, Team, SubTeam, WorkType, \
    WorkSite,BacCategory,BusinessCategory,FunctionalCategory,ImpactScope,Phase,RiskIssueCategory,SubSystemCategory,\
    TestType,RiskScope,RiskResponseType
from import_export.admin import ImportExportModelAdmin


class StatusInline(admin.TabularInline):
    model = Status
    extra = 0
    max_num = 100
    classes = ['collapse']
    classes = ('grp-collapse grp-open',)


class TeamInline(admin.TabularInline):
    model = Team
    extra = 0
    max_num = 100
    classes = ['collapse']
    classes = ('grp-collapse grp-open',)


class SubTeamInline(admin.TabularInline):
    model = SubTeam
    extra = 0
    max_num = 100
    classes = ['collapse']
    classes = ('grp-collapse grp-open',)


class DelayReasonInline(admin.TabularInline):
    model = DelayReason
    extra = 0
    max_num = 100
    classes = ['collapse']
    classes = ('grp-collapse grp-open',)


class WorkTypeInline(admin.TabularInline):
    model = WorkType
    extra = 0
    max_num = 100
    classes = ['collapse']
    classes = ('grp-collapse grp-open',)


class WorkSiteInline(admin.TabularInline):
    model = WorkSite
    extra = 0
    max_num = 100
    classes = ['collapse']
    classes = ('grp-collapse grp-open',)


@admin.register(Status)
class StatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'status')
    list_display_links = ('id', 'status')


@admin.register(Stage)
class StageAdmin(ImportExportModelAdmin):
    list_display = ('id', 'stage', 'comments')
    list_display_links = ('id', 'stage')


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'comments')
    list_display_links = ('id', 'team')


@admin.register(SubTeam)
class SubTeamAdmin(ImportExportModelAdmin):
    list_display = ('id', 'subTeam', 'comments')
    list_display_links = ('id', 'subTeam')


@admin.register(DelayReason)
class DelayReasonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'delayReason', 'comments')
    list_display_links = ('id', 'delayReason')


@admin.register(WorkType)
class WorkTypeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'workType', 'comments')
    list_display_links = ('id', 'workType')


@admin.register(WorkSite)
class WorkSiteAdmin(ImportExportModelAdmin):
    list_display = ('id', 'workSite', 'comments')
    list_display_links = ('id', 'workSite')


@admin.register(BacCategory)
class BacCategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'bacCategory', 'comments')
    list_display_links = ('id', 'bacCategory')


@admin.register(BusinessCategory)
class BusinessCategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'businessCategory', 'comments')
    list_display_links = ('id', 'businessCategory')


@admin.register(FunctionalCategory)
class FunctionalCategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'functionalCategory', 'comments')
    list_display_links = ('id', 'functionalCategory')


@admin.register(ImpactScope)
class ImpactScopeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'impactScope', 'comments')
    list_display_links = ('id', 'impactScope')


@admin.register(Phase)
class PhaseAdmin(ImportExportModelAdmin):
    list_display = ('id', 'phase', 'comments')
    list_display_links = ('id', 'phase')


@admin.register(RiskIssueCategory)
class RiskIssueCategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'riskIssueCategory', 'comments')
    list_display_links = ('id', 'riskIssueCategory')


@admin.register(SubSystemCategory)
class SubSystemCategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'subSystemCategory', 'comments')
    list_display_links = ('id', 'subSystemCategory')


@admin.register(TestType)
class TestTypeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'testType', 'comments')
    list_display_links = ('id', 'testType')


@admin.register(RiskScope)
class RiskScopeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'riskScope', 'comments')
    list_display_links = ('id', 'riskScope')


@admin.register(RiskResponseType)
class RiskResponseTypeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'riskResponseType', 'comments')
    list_display_links = ('id', 'riskResponseType')
