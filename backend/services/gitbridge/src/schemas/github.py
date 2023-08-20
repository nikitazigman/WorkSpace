from datetime import datetime
from src.schemas.common import CommonSchema
from enum import StrEnum


class GithubIssueAction(StrEnum):
    assigned = "assigned"
    closed = "closed"
    deleted = "deleted"
    demilestoned = "demilestoned"
    edited = "edited"
    labeled = "labeled"
    locked = "locked"
    milestoned = "milestoned"
    opened = "opened"
    pinned = "pinned"
    reopened = "reopened"
    transferred = "transferred"
    unassigned = "unassigned"
    unlabeled = "unlabeled"
    unlocked = "unlocked"
    unpinned = "unpinned"


class GithubPullRequestAction(StrEnum):
    assigned = "assigned"
    auto_merge_disabled = "auto_merge_disabled"
    auto_merge_enabled = "auto_merge_enabled"
    closed = "closed"
    converted_to_draft = "converted_to_draft"
    demilestoned = "demilestoned"
    dequeued = "dequeued"
    edited = "edited"
    enqueued = "enqueued"
    labeled = "labeled"
    locked = "locked"
    milestoned = "milestoned"
    opened = "opened"
    ready_for_review = "ready_for_review"
    reopened = "reopened"
    review_request_removed = "review_request_removed"
    review_requested = "review_requested"
    synchronize = "synchronize"
    unassigned = "unassigned"
    unlabeled = "unlabeled"
    unlocked = "unlocked"


class GithubUser(CommonSchema):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool


class GithubIssueReaction(CommonSchema):
    url: str
    total_count: int
    laugh: int
    hooray: int
    confused: int
    heart: int
    rocket: int
    eyes: int


class GithubIssue(CommonSchema):
    url: str
    repository_url: str
    labels_url: str
    comments_url: str
    events_url: str
    html_url: str
    id: int
    node_id: str
    number: int
    title: str
    user: GithubUser
    labels: list
    state: str
    locked: bool
    assignees: list[GithubUser]
    milestone: str | None
    comments: int
    created_at: datetime
    updated_at: datetime
    closed_at: datetime | None
    author_association: str
    active_lock_reason: str | None
    body: str
    reactions: GithubIssueReaction
    timeline_url: str
    performed_via_github_app: str | None
    state_reason: str | None


class GithubRepository(CommonSchema):
    id: int
    node_id: str
    name: str
    full_name: str
    private: bool
    owner: GithubUser
    html_url: str
    description: str | None
    fork: bool
    url: str
    forks_url: str
    keys_url: str
    collaborators_url: str
    teams_url: str
    hooks_url: str
    issue_events_url: str
    events_url: str
    assignees_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    git_tags_url: str
    git_refs_url: str
    trees_url: str
    statuses_url: str
    languages_url: str
    stargazers_url: str
    contributors_url: str
    subscribers_url: str
    subscription_url: str
    commits_url: str
    git_commits_url: str
    comments_url: str
    issue_comment_url: str
    contents_url: str
    compare_url: str
    merges_url: str
    archive_url: str
    downloads_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    deployments_url: str
    created_at: datetime
    updated_at: datetime
    pushed_at: datetime
    git_url: str
    ssh_url: str
    clone_url: str
    svn_url: str
    homepage: str | None
    size: int
    stargazers_count: int
    watchers_count: int
    language: str | None
    has_issues: bool
    has_projects: bool
    has_downloads: bool
    has_wiki: bool
    has_pages: bool
    has_discussions: bool
    forks_count: int
    mirror_url: str | None
    archived: bool
    disabled: bool
    open_issues_count: int
    license: dict
    allow_forking: bool
    is_template: bool
    web_commit_signoff_required: bool
    topics: list
    visibility: str
    forks: int
    open_issues: int
    watchers: int
    default_branch: str


class GitHubCommonPayload(CommonSchema):
    action: str
    repository: GithubRepository
    sender: GithubUser


class GitHubIssuePayload(GitHubCommonPayload):
    issue: GithubIssue


class GitHubPullRequestPayload(GitHubCommonPayload):
    assignee: GithubUser | None
    pull_request: dict  # TODO: Implement GitHubPullRequest
    number: int | None
