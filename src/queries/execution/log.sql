with pre as (
    select distinct created_at::text as ca,
                    '`' ||
                    right((created_at + INTERVAL '3 hour')::date::text, 8) || ' ' ||
                    left((created_at + INTERVAL '3 hour')::time::text, 5) || ' - ' ||
                    case
                        when action = 'answers/create' then 'Завершено ✅'
                        when action = 'attachments/index' then 'Прикреплен файл'
                        when action = 'backups/create' then 'Бэкап сохранен'
                        when action = 'backups/show' then 'Бэкап восстановлен'
                        when action = 'execution/cancel' then 'Отказ'
                        when action = 'executions/assign' then 'В работе'
                        when action = 'executions/cancel' then 'Отказ'
                        else action end || ' ' ||
                    case when data::json ->> 'response_code' = '200' then '' else '(⛔️ Ошибка)' end || E'`\n' as line
    from execution_log
    where execution_id = __arg__
    order by ca desc
    limit 8
),  c as (
    select execution_id, count(execution_id) as c
    from execution_log
    where execution_id = __arg__
    group by execution_id
), final (fsort, tab) as (
select case when c.c > 8 then '…' else null end as line, case when c.c > 8 then '`…`' else null end as ca from c
union all
select ca, line from pre
order by ca
    )
select tab from final
