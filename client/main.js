// Smooth scrolling for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });

            // Close mobile menu if open
            document.getElementById('navMenu').classList.remove('active');
        }
    });
});

// Mobile menu toggle
document.getElementById('menuToggle').addEventListener('click', function () {
    document.getElementById('navMenu').classList.toggle('active');
});

// Heart prediction form handling
const heartForm = document.getElementById('heartForm');
const resultsSection = document.getElementById('results');
const progressCircle = document.getElementById('progressCircle');
const riskPercentage = document.getElementById('riskPercentage');
const riskLevel = document.getElementById('riskLevel');
const riskFactorsList = document.getElementById('riskFactorsList');
const suggestionsList = document.getElementById('suggestionsList');
const resetBtn = document.getElementById('resetBtn');

// Function to calculate heart disease risk (simplified algorithm)
function calculateRisk(data) {
    let baseRisk = 0;
    const riskFactors = [];

    // Age factor
    if (data.age > 60) {
        baseRisk += 15;
        riskFactors.push("Tuổi cao");
    } else if (data.age > 45) {
        baseRisk += 10;
    }

    // Gender factor
    if (data.gender === "male") {
        baseRisk += 5;
    }

    // Cholesterol factor
    if (data.cholesterol > 240) {
        baseRisk += 20;
        riskFactors.push("Cholesterol cao");
    } else if (data.cholesterol > 200) {
        baseRisk += 10;
        riskFactors.push("Cholesterol hơi cao");
    }

    // Blood pressure factor
    if (data.systolic > 140 || data.diastolic > 90) {
        baseRisk += 15;
        riskFactors.push("Huyết áp cao");
    } else if (data.systolic > 120 || data.diastolic > 80) {
        baseRisk += 5;
        riskFactors.push("Tiền cao huyết áp");
    }

    // Smoking factor
    if (data.smoking) {
        baseRisk += 15;
        riskFactors.push("Hút thuốc");
    }

    // Activity factor
    if (data.activity === "low") {
        baseRisk += 10;
        riskFactors.push("Ít vận động");
    } else if (data.activity === "moderate") {
        baseRisk += 5;
    }

    // Family history factor
    if (data.familyHistory) {
        baseRisk += 15;
        riskFactors.push("Tiền sử gia đình");
    }

    // Cap the risk at 95%
    let risk = Math.min(baseRisk, 95);

    return {
        percentage: risk,
        factors: riskFactors
    };
}

// Function to generate suggestions based on risk factors
function generateSuggestions(riskFactors) {
    const suggestions = [];

    // Default suggestion
    suggestions.push({
        icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                </svg>`,
        text: "Kiểm tra sức khỏe định kỳ để theo dõi các chỉ số tim mạch"
    });

    // Add specific suggestions based on risk factors
    if (riskFactors.includes("Cholesterol cao") || riskFactors.includes("Cholesterol hơi cao")) {
        suggestions.push({
            icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <path d="M8 14s1.5 2 4 2 4-2 4-2"></path>
                        <line x1="9" y1="9" x2="9.01" y2="9"></line>
                        <line x1="15" y1="9" x2="15.01" y2="9"></line>
                    </svg>`,
            text: "Giảm lượng cholesterol thông qua chế độ ăn cân bằng và tập thể dục đều đặn"
        });
    }

    if (riskFactors.includes("Huyết áp cao") || riskFactors.includes("Tiền cao huyết áp")) {
        suggestions.push({
            icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
                    </svg>`,
            text: "Hạn chế ăn mặn và tập các phương pháp giảm stress để kiểm soát huyết áp"
        });
    }

    if (riskFactors.includes("Hút thuốc")) {
        suggestions.push({
            icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>`,
            text: "Bỏ thuốc lá ngay để cải thiện sức khỏe tim mạch và giảm nguy cơ đột quỵ"
        });
    }

    if (riskFactors.includes("Ít vận động")) {
        suggestions.push({
            icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <polygon points="10 8 16 12 10 16 10 8"></polygon>
                    </svg>`,
            text: "Tăng cường hoạt động thể chất với ít nhất 150 phút vận động mỗi tuần"
        });
    }

    // Always add doctor suggestion for medium to high risk
    suggestions.push({
        icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 12h18M3 6h18M3 18h18"></path>
                </svg>`,
        text: "Tư vấn với bác sĩ để đánh giá tình trạng sức khỏe tim mạch của bạn"
    });

    return suggestions.slice(0, 4); // Return max 4 suggestions
}

// Form submission handler
heartForm.addEventListener('submit', function (e) {
    e.preventDefault();

    // Collect form data
    const formData = {
        age: parseInt(document.getElementById('age').value),
        gender: document.getElementById('gender').value,
        cholesterol: parseInt(document.getElementById('cholesterol').value),
        systolic: parseInt(document.getElementById('systolic').value),
        diastolic: parseInt(document.getElementById('diastolic').value),
        smoking: document.getElementById('smoking').checked,
        activity: document.getElementById('activity').value,
        familyHistory: document.getElementById('familyHistory').checked
    };

    // Calculate risk
    const riskResult = calculateRisk(formData);

    // Generate risk level text
    let riskLevelText = '';
    let riskClass = '';

    if (riskResult.percentage < 20) {
        riskLevelText = "Thấp";
        riskClass = "low";
    } else if (riskResult.percentage < 50) {
        riskLevelText = "Trung Bình";
        riskClass = "medium";
    } else {
        riskLevelText = "Cao";
        riskClass = "high";
    }

    // Update progress circle
    const circumference = 2 * Math.PI * 90;
    const offset = circumference - (riskResult.percentage / 100) * circumference;
    progressCircle.style.strokeDashoffset = offset;

    // Set color based on risk level
    if (riskClass === "low") {
        progressCircle.style.stroke = getComputedStyle(document.documentElement).getPropertyValue('--green') || "#2ECC71";
    } else if (riskClass === "medium") {
        progressCircle.style.stroke = getComputedStyle(document.documentElement).getPropertyValue('--yellow') || "#F1C40F";
    } else {
        progressCircle.style.stroke = getComputedStyle(document.documentElement).getPropertyValue('--red') || "#E74C3C";
    }

    // Update risk percentage text
    riskPercentage.textContent = riskResult.percentage + "%";

    // Update risk level text
    riskLevel.innerHTML = `Mức: <span class="${riskClass}">${riskLevelText}</span>`;

    // Update risk factors list
    riskFactorsList.innerHTML = '';
    if (riskResult.factors.length > 0) {
        riskResult.factors.forEach(factor => {
            const riskFactorElement = document.createElement('span');
            riskFactorElement.className = 'risk-factor';
            riskFactorElement.textContent = factor;
            riskFactorsList.appendChild(riskFactorElement);
        });
    } else {
        const riskFactorElement = document.createElement('span');
        riskFactorElement.className = 'risk-factor';
        riskFactorElement.textContent = 'Không có yếu tố nguy cơ đáng kể';
        riskFactorsList.appendChild(riskFactorElement);
    }

    // Generate and update suggestions
    const suggestions = generateSuggestions(riskResult.factors);
    suggestionsList.innerHTML = '';
    suggestions.forEach(suggestion => {
        const suggestionElement = document.createElement('div');
        suggestionElement.className = 'suggestion-item';
        suggestionElement.innerHTML = `
                    <div class="suggestion-icon">
                        ${suggestion.icon}
                    </div>
                    <div>${suggestion.text}</div>
                `;
        suggestionsList.appendChild(suggestionElement);
    });

    // Show results section with animation
    resultsSection.style.display = 'block';
    setTimeout(() => {
        resultsSection.classList.add('active');
        // Scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);
});

// Reset button handler
resetBtn.addEventListener('click', function () {
    // Reset form
    heartForm.reset();

    // Hide results
    resultsSection.classList.remove('active');
    setTimeout(() => {
        resultsSection.style.display = 'none';
    }, 300);

    // Scroll to form top
    document.querySelector('.form-title').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
});

// Initialize progress circle
progressCircle.style.strokeDasharray = 2 * Math.PI * 90;