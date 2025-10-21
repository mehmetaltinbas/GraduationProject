import { useEffect, useState } from "react";
import axios from "axios";

const API = "http://127.0.0.1:8000";

export default function App() {
  const [status, setStatus] = useState("Checking...");
  const [resp, setResp] = useState(null);
  const [file, setFile] = useState(null);
//test
  useEffect(() => {
    axios.get(`${API}/health/`)
      .then(r => setStatus(r.data.status))
      .catch(() => setStatus("Failed"));
  }, []);

  const handlePredict = async () => {
    if (!file) return;
    const form = new FormData();
    form.append("file", file);
    const { data } = await axios.post(`${API}/api/predict`, form, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    setResp(data);
  };

  return (
    <div style={{ fontFamily: "Arial", padding: 24 }}>
      <h1>Weapon Detection — Frontend Test</h1>
      <p>Backend status: <b>{status}</b></p>

      <div style={{ marginTop: 16 }}>
        <input type="file" accept="image/*" onChange={(e)=>setFile(e.target.files[0])}/>
        <button onClick={handlePredict} style={{ marginLeft: 8 }}>Detect</button>
      </div>

      <pre style={{ background:"#f6f6f6", padding:12, marginTop:16 }}>
        {resp ? JSON.stringify(resp, null, 2) : "No response yet"}
      </pre>
    </div>
  );
}

