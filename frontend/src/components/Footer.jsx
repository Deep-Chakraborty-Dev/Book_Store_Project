// Footer.js
import React from "react";

function Footer() {
  return (

    <footer style={styles.footer} className="items-center bg-gray-400">
      <div className="flex flex-col md:flex-row justify-between gap-8 px-10">
        <div style={styles.section} className="items-center">
          <h3 className="text-yellow-300">Book Nest</h3>
          <p>Your one-stop shop for books of all genres.</p>
        </div>

        <div style={styles.section}>
          <h4 className="text-yellow-300">Quick Links</h4>
          <ul style={styles.list} className="text-shadow-amber-200">
            <li><a href="/" style={styles.link}>Home</a></li>
          </ul>
        </div>

        <div style={styles.section}>
          <h4 className="text-yellow-300">Contact</h4>
          <p>Email: support@Booknest.com</p>
          <p>Phone: +1 234 567 890</p>
        </div>
      </div>

      <div style={styles.bottom}>
        © {new Date().getFullYear()} Book Nest. All rights reserved.
      </div>
    </footer>
  );
}

const styles = {
  footer: {
    backgroundColor: "#222",
    color: "#fff",
    padding: "40px 20px 20px",
    marginTop: "40px",
  },
  container: {
    display: "flex",
    justifyContent: "space-between",
    flexWrap: "wrap",
  },
  section: {
    flex: "1",
    minWidth: "200px",
    marginBottom: "20px",
  },
  list: {
    listStyle: "none",
    padding: 0,
  },
  link: {
    color: "#ccc",
    textDecoration: "none",
  },
  bottom: {
    textAlign: "center",
    borderTop: "1px solid #444",
    paddingTop: "15px",
    marginTop: "20px",
    fontSize: "14px",
  },
};

export default Footer;
