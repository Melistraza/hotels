from rest_framework import throttling


class UpdateLimitThrottle(throttling.UserRateThrottle):

    def get_rate(self):
        return '1/min'

    def allow_request(self, request, view):
        status = super(UpdateLimitThrottle, self).allow_request(request, view)
        if request.method in ['PUT', 'PATCH']:
            return status
        return self.throttle_success()
