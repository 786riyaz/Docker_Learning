import mysql from 'mysql2/promise';
import dotenv from 'dotenv';

dotenv.config();

// Connection config (use env vars or defaults)
const MYSQL_HOST = process.env.MYSQL_HOST || 'host.docker.internal';
// const MYSQL_HOST = process.env.MYSQL_HOST || 'localhost'; // uncomment for non-Docker setup
const MYSQL_PORT = parseInt(process.env.MYSQL_PORT || '3306');
const MYSQL_USER = process.env.MYSQL_USER || 'root';
const MYSQL_PASSWORD = process.env.MYSQL_PASSWORD || '';
const MYSQL_DB = process.env.MYSQL_DB || 'e-commerce'; // DB shown in your phpMyAdmin URL

async function connectMysql(host, port, user, password, database) {
  try {
    const conn = await mysql.createConnection({
      host,
      port,
      user,
      password,
      database,
      waitForConnections: true,
      connectionLimit: 1,
      queueLimit: 0,
    });
    console.log(`✅ Connected to MySQL DB '${database}' on ${host}:${port}`);
    return conn;
  } catch (e) {
    console.error('❌ MySQL connection error:', e.message);
    throw e;
  }
}

async function fetchProducts(conn, database = MYSQL_DB, table = 'products') {
  try {
    // Backticks escape identifiers to allow hyphens in database/table names and avoid injection
    const dbQuoted = `\`${database.replace(/`/g, '')}\``;
    const tableQuoted = `\`${table.replace(/`/g, '')}\``;
    const sql = `SELECT * FROM ${dbQuoted}.${tableQuoted};`;
    
    const [rows] = await conn.execute(sql);
    console.log('📄 Products from DB:');
    rows.forEach(r => console.log(r));
  } catch (e) {
    console.error('❌ Error fetching products:', e.message);
  } finally {
    if (conn) {
      await conn.end();
    }
  }
}

(async () => {
  const conn = await connectMysql(MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB);
  await fetchProducts(conn);
})();