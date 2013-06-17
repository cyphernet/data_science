SELECT LEFT(created_at, 7) as month, repository_language, COUNT(*) as pushes
FROM [githubarchive:github.timeline]
WHERE type='PushEvent'
GROUP BY month, repository_language
ORDER BY month DESC