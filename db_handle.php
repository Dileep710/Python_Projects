<?php
$host = 'localhost';
$dbname = 'IceCreamShop';
$username = 'root';
$password = '';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
}
?>

<?php
include 'connect.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Get customer details and order items
    $customer_name = $_POST['customer_name'];
    $customer_mobile = $_POST['customer_mobile'];
    
    // Insert Order into Orders table
    $stmt = $pdo->prepare("INSERT INTO Orders (customer_name, customer_mobile) VALUES (?, ?)");
    $stmt->execute([$customer_name, $customer_mobile]);
    $order_id = $pdo->lastInsertId(); // Get the inserted order ID

    // Insert Order Items
    $order_items = json_decode($_POST['order_items'], true);  // JSON format from Python
    foreach ($order_items as $item) {
        $stmt = $pdo->prepare("INSERT INTO OrderItems (order_id, product_type, product_name, quantity, price) 
                               VALUES (?, ?, ?, ?, ?)");
        $stmt->execute([$order_id, $item['type'], $item['name'], $item['quantity'], $item['price']]);
    }

    echo "Order added successfully!";
}
?>

<?php
include 'connect.php';

$stmt = $pdo->query("SELECT * FROM Orders");
$orders = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($orders);
?>
