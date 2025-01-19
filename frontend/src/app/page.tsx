import Image from "next/image";
import styles from "./page.module.css";
import Link from "next/link";

export default function Home() {
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
        <div id="front-image">
          <div id="front-screen"></div>
          <div id="title-holder">
            <h1 id="title">CyberAgent</h1>
            <h2 id="title-desc">AI-Powered Vulnerability Detection</h2>
            <Link id="title-btn" className="button" href="/app">
              Get Started{" "}
            </Link>
          </div>
        </div>

        <div id="about" className="text-block">
          <h2>About CyberAgent</h2>
          <p>
            CyberAgent is an AI-powered security developer tool that detects
            back-end vulnerabilities.
          </p>
        </div>

        <div id="footer">
          <hr />
          <div className="footer-block">
            <p>
              <b>CyberAgent</b>
            </p>
            <p>
              <Link className="link" href="/">
                About
              </Link>
              <br />
              <Link className="link" href="/app">
                App
              </Link>
            </p>
          </div>
        </div>
      </div>
    </>
  );
}
