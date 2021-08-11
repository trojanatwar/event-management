from flask import Flask
from flask_restful import Resource, Api, abort, fields, marshal_with, abort
import models as md



wApp = Flask(__name__)
rApi = Api(wApp)

resource_field = {
    "id": fields.String,
    "event_name": fields.String,
    "evedate": fields.String,
    "ticket_cnt": fields.Integer,
}

class Events(Resource):
    @marshal_with(resource_field)
    def get(self, event_id):
        result = md.getEvent(event_id)
        return result

class CreateEvent(Resource):

    @marshal_with(resource_field)
    def post(self, event_id, event_name, date, ticket_cnt):
        if md.addEvent(event_id, event_name, date, ticket_cnt):
            return abort(200, message="Successfully created event.")
        else:
            return abort(404, message="Record is already created")

class AvailableTickets(Resource):

    def get(self, event_id):
        result = md.getEvent(event_id)
        for r in result:
            result = r["ticket_cnt"]
        
        return {"ticket_avai": result}


class EventTickets(Resource):

    def get(self):
        pass

class AddTickets(Resource):
    def put(self, event_id, val):
        data = md.getEvent(event_id)
        for r in data:
            cnt = r["ticket_cnt"]
        
        val = cnt + val
        resp = md.updateEvent(event_id, val)

        return {"respo": resp}

class RedeemTickets(Resource):

    def put(self, event_id, number_of_tickets):
        data = md.getEvent(event_id)
        for r in data:
            cnt = r["ticket_cnt"]

        if cnt < 0:
            return abort(410, message="GONE")
        else:
            number_of_tickets = cnt - number_of_tickets
            md.updateEvent(event_id, number_of_tickets)
            return "OK", 201

rApi.add_resource(Events, '/events/<int:event_id>/')
rApi.add_resource(CreateEvent, '/events/create/<int:event_id>/<string:event_name>/<string:date>/<int:ticket_cnt>')
rApi.add_resource(AvailableTickets, '/events/available/<int:event_id>/')
rApi.add_resource(AddTickets, '/events/add/<int:event_id>/<int:val>')
rApi.add_resource(RedeemTickets, '/events/redeem/<int:event_id>/<int:number_of_tickets>')


if __name__ == "__main__":
    wApp.run(debug=True, host='0.0.0.0')


