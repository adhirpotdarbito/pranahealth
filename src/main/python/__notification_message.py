class NotificationMessage():
    def __init_(self):
        self.notification_type = None
        self.notification_category = None
        self.message_template = ""
        self.message_template_parameters = {}
        self.target_audience = []

    def setNotificationType(self, notification_type):
        self.notification_type = notification_type
 
    def getNotificationType(self):
        return self.notification_type

    def setNotificationCategory(self, notification_category):
        self.notification_category = notification_category

    def getNotificationCategory(self):
        return self.notification_category

    def setMessageTemplate(self, message_template):
        self.message_template = message_template

    def setMessageTemplateParameters(self, template_parameters):
        self.message_template_parameters = template_parameters

    def setTargetAudience(self, target_audience):
        self.target_audience = target_audience

    def getMessageTemplate(self):
        return self.message_template

    def getMessageTemplateParameters(self):
        return self.message_template_parameters
 
    def getTargetAudience(self):
        return self.target_audience
