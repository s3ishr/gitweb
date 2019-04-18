#!/bin/sh

export GIT_PROJECT_ROOT="++GIT_PROJECT_ROOT++"
export GIT_HTTP_EXPORT_ALL

exec /usr/libexec/git-core/git-http-backend
