select
    Register.contest_id,
    round(
        count(Users.user_id) /(
            select
                count(Users.user_id)
            from
                Users
        ) * 100,
        2
    ) as percentage
from
    Register
    join Users on Register.user_id = Users.user_id
group by
    Register.contest_id
order by
    percentage desc,
    contest_id 