insert into bot.log_status (created_at, message, data, error, app_name)
select now(), E'{0}'::varchar, E'{1}'::varchar, E'{2}'::varchar, E'{3}'::varchar