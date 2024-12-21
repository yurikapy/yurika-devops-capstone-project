import pytest
from service.models import Account, db
from service import app

# Setup untuk aplikasi
@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/postgres"
    client = app.test_client()
    with app.app_context():
        db.create_all()
    yield client
    with app.app_context():
        db.drop_all()

# Tes untuk membuat akun baru
def test_create_account(client):
    account_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "balance": 1000
    }
    
    # Kirim permintaan POST untuk membuat akun
    response = client.post('/accounts', json=account_data)

    # Pastikan status code adalah HTTP_201_CREATED (Akun berhasil dibuat)
    assert response.status_code == 201

    # Ambil ID akun yang baru dibuat dari response JSON
    account_id = response.get_json()['id']

    # Ambil akun tersebut menggunakan GET
    response = client.get(f'/accounts/{account_id}')

    # Pastikan status code adalah HTTP_200_OK
    assert response.status_code == 200

    # Verifikasi data yang dikembalikan
    data = response.get_json()
    assert data["name"] == account_data["name"]
    assert data["email"] == account_data["email"]
    assert data["balance"] == account_data["balance"]

# Tes untuk mencoba membuat akun dengan data yang tidak lengkap
def test_create_account_bad_request(client):
    account_data = {
        "name": "John Doe"
        # Data lainnya hilang
    }
    
    response = client.post('/accounts', json=account_data)
    
    # Pastikan permintaan tersebut gagal dengan status code HTTP_400_BAD_REQUEST
    assert response.status_code == 400
