select
    Signups.user_id,
    round(
        sum(if(Confirmations.action = 'confirmed', 1, 0)) / count(1),
        2
    ) as confirmation_rate
from
    Signups
    left join Confirmations on Confirmations.user_id = Signups.user_id
group by
    Signups.user_id