import flask
import flask_restplus

api_v1 = flask.Blueprint('api', __name__, url_prefix='/api/AssetsService/accounts')

api = flask_restplus.Api(api_v1, version='1.0', title='Example REST Service',
                         description='Example REST Service to get a TT User',
                         )

ns = api.namespace('assets', description='Assets available')


ASSETS = {
    'asset1': {'id': 'XBTH19', 'currency': 'XBTH19', 'balance': 5.0, 'holds': 0.0, 'available': 5.0},
    'asset2': {'id': 'XBt', 'currency': 'XBt', 'balance': 0.00700044, 'holds': 0.0, 'available': 0.00698473},
}


@ns.route('/<string:asset_id>')
@api.doc(responses={404: 'Asset not found'}, params={'asset_id': 'The Asset ID'})
class Asset(flask_restplus.Resource):
    """Show a single asset item and lets you delete them"""

    @api.doc(description='Get asset information')
    def get(self, asset_id):
        """Fetch a given resource"""
        return ASSETS[asset_id]


@ns.route('/')
class AssetList(flask_restplus.Resource):
    """Shows a list of all assets, and lets you POST to add new assets"""

    def get(self):
        """List all assets"""
        return ASSETS


if __name__ == '__main__':
    """Example of usage: GET http://127.0.0.1:5000/api/accounts/assets/asset1"""
    app = flask.Flask(__name__)
    app.register_blueprint(api_v1)
    app.run(debug=True)
