select
case when i.name is null then ' ' else i.name || ' - ' end || case when s.name is null then ' ' else s.name end || E'\n\n' as global_name,
'`      КНД: ' || e.id || E'\n`' as exec_id,
'`   статус: ' || case
    when e.status = 1 then 'в_работе'
    when e.status = 3 then 'отправлено'
    else 'в_нераспред.'  end || ''  || E'`\n' as status_name,
'`   начало: ' || (e.start_time + INTERVAL '3 hour')::date::text || ''  || E'`\n' as e_sd,
'`завершено: ' || (e.completed_at + INTERVAL '3 hour')::date::text || ' ✅'  || E'`\n' as e_cd,
'`окончание: ' || (e.plan_time + INTERVAL '3 hour')::date::text || ''  || E'`\n' as e_ed,
-- '`   проект: ' || p.id::text    || ''  || E'`\n' as p_id,
-- '' || p.name ::text  || ''  || E'\n' as p_name,
--'` компания: ' ||
E'\n`🏢 ' || c.id::text || ' - ' || p.id::text || ''  || E'`\n' as c_id,
'' || c.name ::text || case when c.inn is not null then ' (' ||c.inn || ')' else '' end  || E'\n' as c_name,
--'`назначено: ' ||
case when a.id = -1 then ' ' else '👤 `' || a.id::text || E'`\n' end ||
case when a.label::text = 'В_нераспределенных' then '🚷 В нераспределенных' else a.label::text end  || ''  || E'\n' as a_name,
case when a.email::text = 'na@na.na' then null
else  replace( replace(a.email::text, '_', '\_'), '*', '\*') end  || ''  || E'\n' as a_email

from execution e
join actor a on e.actor_id = a.id
join issue_task it on e.issue_task_id = it.id
left join issue i on it.id = i.id
left join project p on e.project_id = p.id
left join company c on p.company_id = c.id
left join stage s on e.stage_id = s.id
-- left join mbu_report_for_bot d on e.id = d."номер задания"
where e.id = __arg__::bigint
