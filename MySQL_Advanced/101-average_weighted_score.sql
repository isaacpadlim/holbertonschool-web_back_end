-- Task 13
-- Script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS U,
           (SELECT c.user_id, SUM(c.score * p.weight) / SUM(p.weight) AS w_avg
            FROM corrections AS c
            JOIN projects AS p ON c.project_id = p.id
            GROUP BY c.user_id) AS WA
    SET U.average_score = WA.w_avg
    WHERE U.id = WA.user_id;
END //
DELIMITER ;
