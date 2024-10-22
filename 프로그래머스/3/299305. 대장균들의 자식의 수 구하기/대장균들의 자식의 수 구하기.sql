SELECT A.ID, COUNT(B.PARENT_ID) as CHILD_COUNT
FROM ECOLI_DATA as A
LEFT JOIN ECOLI_DATA as B
ON A.ID = B.PARENT_ID
GROUP BY 1
ORDER BY 1