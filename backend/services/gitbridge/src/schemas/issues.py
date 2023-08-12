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


class GihubIssueReaction(CommonSchema):
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
    reactions: GihubIssueReaction
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


class GithubIssuePayload(CommonSchema):
    action: GithubIssueAction
    issue: GithubIssue
    repository: GithubRepository
    sender: GithubUser


data = {
    "action": "assigned",
    "issue": {
        "url": "https://api.github.com/repos/nikitazigman/test_repo/issues/2",
        "repository_url": "https://api.github.com/repos/nikitazigman/test_repo",
        "labels_url": "https://api.github.com/repos/nikitazigman/test_repo/issues/2/labels{/name}",
        "comments_url": "https://api.github.com/repos/nikitazigman/test_repo/issues/2/comments",
        "events_url": "https://api.github.com/repos/nikitazigman/test_repo/issues/2/events",
        "html_url": "https://github.com/nikitazigman/test_repo/issues/2",
        "id": 1848092205,
        "node_id": "I_kwDOH8Irr85uJ6Yt",
        "number": 2,
        "title": "asda",
        "user": {
            "login": "nikitazigman",
            "id": 60356768,
            "node_id": "MDQ6VXNlcjYwMzU2NzY4",
            "avatar_url": "https://avatars.githubusercontent.com/u/60356768?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/nikitazigman",
            "html_url": "https://github.com/nikitazigman",
            "followers_url": "https://api.github.com/users/nikitazigman/followers",
            "following_url": "https://api.github.com/users/nikitazigman/following{/other_user}",
            "gists_url": "https://api.github.com/users/nikitazigman/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/nikitazigman/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/nikitazigman/subscriptions",
            "organizations_url": "https://api.github.com/users/nikitazigman/orgs",
            "repos_url": "https://api.github.com/users/nikitazigman/repos",
            "events_url": "https://api.github.com/users/nikitazigman/events{/privacy}",
            "received_events_url": "https://api.github.com/users/nikitazigman/received_events",
            "type": "User",
            "site_admin": False,
        },
        "labels": [],
        "state": "open",
        "locked": False,
        "assignee": {
            "login": "nikitazigman",
            "id": 60356768,
            "node_id": "MDQ6VXNlcjYwMzU2NzY4",
            "avatar_url": "https://avatars.githubusercontent.com/u/60356768?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/nikitazigman",
            "html_url": "https://github.com/nikitazigman",
            "followers_url": "https://api.github.com/users/nikitazigman/followers",
            "following_url": "https://api.github.com/users/nikitazigman/following{/other_user}",
            "gists_url": "https://api.github.com/users/nikitazigman/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/nikitazigman/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/nikitazigman/subscriptions",
            "organizations_url": "https://api.github.com/users/nikitazigman/orgs",
            "repos_url": "https://api.github.com/users/nikitazigman/repos",
            "events_url": "https://api.github.com/users/nikitazigman/events{/privacy}",
            "received_events_url": "https://api.github.com/users/nikitazigman/received_events",
            "type": "User",
            "site_admin": False,
        },
        "assignees": [
            {
                "login": "nikitazigman",
                "id": 60356768,
                "node_id": "MDQ6VXNlcjYwMzU2NzY4",
                "avatar_url": "https://avatars.githubusercontent.com/u/60356768?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/nikitazigman",
                "html_url": "https://github.com/nikitazigman",
                "followers_url": "https://api.github.com/users/nikitazigman/followers",
                "following_url": "https://api.github.com/users/nikitazigman/following{/other_user}",
                "gists_url": "https://api.github.com/users/nikitazigman/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/nikitazigman/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/nikitazigman/subscriptions",
                "organizations_url": "https://api.github.com/users/nikitazigman/orgs",
                "repos_url": "https://api.github.com/users/nikitazigman/repos",
                "events_url": "https://api.github.com/users/nikitazigman/events{/privacy}",
                "received_events_url": "https://api.github.com/users/nikitazigman/received_events",
                "type": "User",
                "site_admin": False,
            }
        ],
        "milestone": None,
        "comments": 0,
        "created_at": "2023-08-12T15:59:25Z",
        "updated_at": "2023-08-12T15:59:25Z",
        "closed_at": None,
        "author_association": "OWNER",
        "active_lock_reason": None,
        "body": "1",
        "reactions": {
            "url": "https://api.github.com/repos/nikitazigman/test_repo/issues/2/reactions",
            "total_count": 0,
            "+1": 0,
            "-1": 0,
            "laugh": 0,
            "hooray": 0,
            "confused": 0,
            "heart": 0,
            "rocket": 0,
            "eyes": 0,
        },
        "timeline_url": "https://api.github.com/repos/nikitazigman/test_repo/issues/2/timeline",
        "performed_via_github_app": None,
        "state_reason": None,
    },
    "assignee": {
        "login": "nikitazigman",
        "id": 60356768,
        "node_id": "MDQ6VXNlcjYwMzU2NzY4",
        "avatar_url": "https://avatars.githubusercontent.com/u/60356768?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nikitazigman",
        "html_url": "https://github.com/nikitazigman",
        "followers_url": "https://api.github.com/users/nikitazigman/followers",
        "following_url": "https://api.github.com/users/nikitazigman/following{/other_user}",
        "gists_url": "https://api.github.com/users/nikitazigman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nikitazigman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nikitazigman/subscriptions",
        "organizations_url": "https://api.github.com/users/nikitazigman/orgs",
        "repos_url": "https://api.github.com/users/nikitazigman/repos",
        "events_url": "https://api.github.com/users/nikitazigman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nikitazigman/received_events",
        "type": "User",
        "site_admin": False,
    },
    "repository": {
        "id": 532818863,
        "node_id": "R_kgDOH8Irrw",
        "name": "test_repo",
        "full_name": "nikitazigman/test_repo",
        "private": True,
        "owner": {
            "login": "nikitazigman",
            "id": 60356768,
            "node_id": "MDQ6VXNlcjYwMzU2NzY4",
            "avatar_url": "https://avatars.githubusercontent.com/u/60356768?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/nikitazigman",
            "html_url": "https://github.com/nikitazigman",
            "followers_url": "https://api.github.com/users/nikitazigman/followers",
            "following_url": "https://api.github.com/users/nikitazigman/following{/other_user}",
            "gists_url": "https://api.github.com/users/nikitazigman/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/nikitazigman/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/nikitazigman/subscriptions",
            "organizations_url": "https://api.github.com/users/nikitazigman/orgs",
            "repos_url": "https://api.github.com/users/nikitazigman/repos",
            "events_url": "https://api.github.com/users/nikitazigman/events{/privacy}",
            "received_events_url": "https://api.github.com/users/nikitazigman/received_events",
            "type": "User",
            "site_admin": False,
        },
        "html_url": "https://github.com/nikitazigman/test_repo",
        "description": None,
        "fork": False,
        "url": "https://api.github.com/repos/nikitazigman/test_repo",
        "forks_url": "https://api.github.com/repos/nikitazigman/test_repo/forks",
        "keys_url": "https://api.github.com/repos/nikitazigman/test_repo/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/nikitazigman/test_repo/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/nikitazigman/test_repo/teams",
        "hooks_url": "https://api.github.com/repos/nikitazigman/test_repo/hooks",
        "issue_events_url": "https://api.github.com/repos/nikitazigman/test_repo/issues/events{/number}",
        "events_url": "https://api.github.com/repos/nikitazigman/test_repo/events",
        "assignees_url": "https://api.github.com/repos/nikitazigman/test_repo/assignees{/user}",
        "branches_url": "https://api.github.com/repos/nikitazigman/test_repo/branches{/branch}",
        "tags_url": "https://api.github.com/repos/nikitazigman/test_repo/tags",
        "blobs_url": "https://api.github.com/repos/nikitazigman/test_repo/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/nikitazigman/test_repo/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/nikitazigman/test_repo/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/nikitazigman/test_repo/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/nikitazigman/test_repo/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/nikitazigman/test_repo/languages",
        "stargazers_url": "https://api.github.com/repos/nikitazigman/test_repo/stargazers",
        "contributors_url": "https://api.github.com/repos/nikitazigman/test_repo/contributors",
        "subscribers_url": "https://api.github.com/repos/nikitazigman/test_repo/subscribers",
        "subscription_url": "https://api.github.com/repos/nikitazigman/test_repo/subscription",
        "commits_url": "https://api.github.com/repos/nikitazigman/test_repo/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/nikitazigman/test_repo/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/nikitazigman/test_repo/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/nikitazigman/test_repo/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/nikitazigman/test_repo/contents/{+path}",
        "compare_url": "https://api.github.com/repos/nikitazigman/test_repo/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/nikitazigman/test_repo/merges",
        "archive_url": "https://api.github.com/repos/nikitazigman/test_repo/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/nikitazigman/test_repo/downloads",
        "issues_url": "https://api.github.com/repos/nikitazigman/test_repo/issues{/number}",
        "pulls_url": "https://api.github.com/repos/nikitazigman/test_repo/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/nikitazigman/test_repo/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/nikitazigman/test_repo/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/nikitazigman/test_repo/labels{/name}",
        "releases_url": "https://api.github.com/repos/nikitazigman/test_repo/releases{/id}",
        "deployments_url": "https://api.github.com/repos/nikitazigman/test_repo/deployments",
        "created_at": "2022-09-05T08:53:47Z",
        "updated_at": "2023-01-29T19:42:32Z",
        "pushed_at": "2022-11-18T12:11:41Z",
        "git_url": "git://github.com/nikitazigman/test_repo.git",
        "ssh_url": "git@github.com:nikitazigman/test_repo.git",
        "clone_url": "https://github.com/nikitazigman/test_repo.git",
        "svn_url": "https://github.com/nikitazigman/test_repo",
        "homepage": None,
        "size": 7,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": None,
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": False,
        "has_pages": False,
        "has_discussions": False,
        "forks_count": 0,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 2,
        "license": {
            "key": "apache-2.0",
            "name": "Apache License 2.0",
            "spdx_id": "Apache-2.0",
            "url": "https://api.github.com/licenses/apache-2.0",
            "node_id": "MDc6TGljZW5zZTI=",
        },
        "allow_forking": True,
        "is_template": False,
        "web_commit_signoff_required": False,
        "topics": [],
        "visibility": "private",
        "forks": 0,
        "open_issues": 2,
        "watchers": 0,
        "default_branch": "master",
    },
    "sender": {
        "login": "nikitazigman",
        "id": 60356768,
        "node_id": "MDQ6VXNlcjYwMzU2NzY4",
        "avatar_url": "https://avatars.githubusercontent.com/u/60356768?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nikitazigman",
        "html_url": "https://github.com/nikitazigman",
        "followers_url": "https://api.github.com/users/nikitazigman/followers",
        "following_url": "https://api.github.com/users/nikitazigman/following{/other_user}",
        "gists_url": "https://api.github.com/users/nikitazigman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nikitazigman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nikitazigman/subscriptions",
        "organizations_url": "https://api.github.com/users/nikitazigman/orgs",
        "repos_url": "https://api.github.com/users/nikitazigman/repos",
        "events_url": "https://api.github.com/users/nikitazigman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nikitazigman/received_events",
        "type": "User",
        "site_admin": False,
    },
}
