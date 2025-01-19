import Link from "next/link";

export default function App() {
  return (
    <>
      <div id="global">
        <div id="top-bar">
          <Link id="top-bar-logo" href="/">
            CyberAgent
          </Link>
          <div id="top-bar-nav">
            <div id="nav-expand">
              <i className="fa-solid fa-bars"></i>
            </div>
            <Link className="top-bar-btn" id="top-bar-home" href="/">
              About
            </Link>
            <Link className="top-bar-btn" id="top-bar-about" href="/app">
              App
            </Link>
          </div>
        </div>
      </div>

      <div id="main">
        <div id="about" className="text-block">
          <h2>About CyberAgent</h2>
          <p>yes</p>
        </div>

        <div id="detect" className="text-block">
          <h2>Detect</h2>
          <input
            id="detect-url"
            className="text-entry"
            type="text"
            placeholder="Enter URL"
          />
          <div id="detect-btn" className="button">
            Scan for Vulnerabilities
          </div>
        </div>

        <div id="detected" className="text-block">
          <h2>Detected Vulnerabilities</h2>
          <p id="detected-status">Scanning... (x%)</p>
          <table>
            <tr>
              <th>#</th>
              <th>Issue</th>
              <th>File</th>
              <th>Details</th>
            </tr>
            <tr>
              <td className="td-right">1</td>
              <td>Insecure Password</td>
              <td>https://www.site.com/login</td>
              <td>
                Password sent as plain text
                <pre>insert_code();</pre>
              </td>
            </tr>
            <tr>
              <td className="td-right">2</td>
              <td>SQL Injection</td>
              <td>https://www.site.com/login</td>
              <td>
                SQL injection possible
                <pre>insert_code();</pre>
              </td>
            </tr>
          </table>
        </div>

        <div id="footer">
          <hr />
          <div className="footer-block">
            <p>
              <b>CyberAgent</b>
            </p>
            <p>
              <Link className="link" target="_blank" href="/">
                About
              </Link>
              <br />
              <Link className="link" target="_blank" href="/app">
                App
              </Link>
            </p>
          </div>
        </div>
      </div>

      <script src="../static/src/app.js"></script>
    </>
  );
}
