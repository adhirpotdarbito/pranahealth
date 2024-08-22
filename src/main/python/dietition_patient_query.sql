USE pranacare;

select uh.provider_id,u.name,count(distinct uh.user_id) from user_history_data uh, users u where u.role = 'DIETITION_ACL' and uh.provider_id = u.id and uh.time_key >= 20190701 and uh.time_key <= 20190731 and u.name not like '%Isana%' and u.name not like '%Adhir%' group by uh.provider_id;

select ud.provider_id,u.name,count(distinct ud.user_id) from user_data_update ud, users u where u.role = 'DIETITION_ACL' and ud.provider_id = u.id and ud.time_key >= 20190701 and ud.time_key <= 20190731 and u.name not like '%Isana%' and u.name not like '%Adhir%' group by ud.provider_id;

select u.id, u.name,count(distinct apm.patient_id) from users u, admin_patient_mapping apm where u.id = apm.admin_id and u.role = 'DIETITION_ACL' and u.name not like '%Isana%' and u.name not like '%Adhir%' and date_format(apm.timestamp, '%Y%m%d') >= 20190701 and date_format(apm.timestamp, '%Y%m%d') < 20190801 group by u.id,u.name;






