import React from "react";

const ProgressBar = ({ step, totalSteps }) => {
    const progress = (step / totalSteps) * 100;

    return (
        <div className="progress-bar">
            <div
                className="progress-bar-fill"
                style={{ width: `${progress}%` }}
            ></div>
        </div>
    );
};

export default ProgressBar;