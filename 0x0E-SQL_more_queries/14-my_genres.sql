-- 14. My genres
SELECT tv_genres.name
FROM tv_genres
JOIN tv_shows
ON tv_genres.id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
