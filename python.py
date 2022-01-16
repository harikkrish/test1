def add_to_acccount_freeeze(self, num, reason=None):
try:
self.logger.info("request to add to list: %r" % (num, reason))
insert_sql = "INSERT INTO list (num, status, w_status, reason, created)VALUES(:num, :status, :w_status, :reason, :created)"
prm = {"num":num, "status":status, "w_status":1, "reason":reason,"created":datetime.now()}
self.db.engine.execute(sql_text(insert_sql), prm)
self.logger.info("add to list sql: {0} : params : {1}".format(sql, prm))
except Exception as ex:
self.logger.error("adding to list: %r" % ex)
