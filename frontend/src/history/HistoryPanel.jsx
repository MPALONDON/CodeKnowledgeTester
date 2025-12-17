import "react";
import {useState, useEffect, use} from "react";
import MCQChallenge from "../challenge/MCQChallenge.jsx";
import style from "./history.module.css";

export default function HistoryPanel(){
    const [history, setHistory] = useState([])
    const [isLoading,setIsLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() =>{
        fetchHistory()
    },[])

    const fetchHistory = async () => {
        setIsLoading(false)
    }

    if (isLoading){
        return <div className={style.loading}>Loading history...</div>
    }

    if (error){
        return <div className={style.errorMessage}>
            <p>{error}</p>
            <button onClick={fetchHistory}></button>

        </div>
    }
    return <div className={style.historyPanel}>
        <h2>History</h2>
        {history.length ===0 ? <p>No Challenge history</p>
            :
            <div className={style.historyList}>
                {history.map((challenge)=>{
                    return <MCQChallenge
                        challenge={challenge}
                        key={challenge.id}
                        showExplanation>
                    </MCQChallenge>
                })}
            </div>
        }
    </div>
}