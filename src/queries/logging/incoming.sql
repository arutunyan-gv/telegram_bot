insert into bot.log_incoming(	  created_at,
                                  message_id,
                                  user_id,
                                  user_name,
                                  user_fio,
                                  chat_id,
                                  chat_name,
                                  command,
                                  message,
                                  app_name
                                  )
select   now(),
         {}::bigint,
         {}::bigint,
        replace('{}', 'None', '')::text,
        replace('{}', 'None', '')::text,
         {}::bigint,
        replace('{}', 'None', '')::text,
        '{}'::text,
        '{}'::text,
        '{}'::text
returning id