select
    Employee.name
from
    Employee
    join (
        select
            managerId
        from
            Employee
        group by
            managerId
        having
            count(managerId) >= 5
    ) as Grouped on Employee.id = Grouped.managerId