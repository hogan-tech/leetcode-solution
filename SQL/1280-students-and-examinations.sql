select
    Students.student_id,
    Students.student_name,
    Subjects.subject_name,
    ifnull (Grouped.attended_exams, 0) as attended_exams
from
    Students
    cross join Subjects
    left join (
        select
            student_id,
            subject_name,
            count(*) as attended_exams
        from
            Examinations
        group by
            student_id,
            subject_name
    ) Grouped on Students.student_id = Grouped.student_id
    and Subjects.subject_name = Grouped.subject_name
order by
    Students.student_id,
    Subjects.subject_name

