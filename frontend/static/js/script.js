// const API_BASE_URL = window.location.origin + '/api';

// // Global state
// let appState = {
//     profile: null,
//     projects: [],
//     skills: []
// };

// document.addEventListener('DOMContentLoaded', function() {
//     initializeApp();
// });

// function initializeApp() {
//     // Load data based on current page
//     if (document.getElementById('profile-content')) {
//         loadProfile();
//     } else if (document.getElementById('projects-content')) {
//         loadProjects();
//     } else if (document.getElementById('search-content')) {
//         setupSearch();
//         loadTopSkills();
//     }
    
//     // Add active class to current page in navigation
//     highlightCurrentPage();
// }

// function highlightCurrentPage() {
//     const currentPath = window.location.pathname;
//     const navLinks = document.querySelectorAll('nav a');
    
//     navLinks.forEach(link => {
//         if (link.getAttribute('href') === currentPath) {
//             link.classList.add('active');
//         }
//     });
// }

// // Profile functions
// async function loadProfile() {
//     try {
//         showLoading('profile-content');
//         const response = await fetch(`${API_BASE_URL}/profile`);
        
//         if (!response.ok) {
//             throw new Error(`HTTP error! status: ${response.status}`);
//         }
        
//         const profile = await response.json();
//         appState.profile = profile;
//         displayProfile(profile);
//     } catch (error) {
//         console.error('Error loading profile:', error);
//         showError('Failed to load profile. Please try again later.');
//     }
// }

// function displayProfile(profile) {
//     const profileContent = document.getElementById('profile-content');
    
//     if (!profile) {
//         profileContent.innerHTML = `
//             <div class="card error-card">
//                 <h3>No Profile Data</h3>
//                 <p>Profile data is not available. Please check if the database is seeded properly.</p>
//             </div>
//         `;
//         return;
//     }
    
//     let profileHTML = `
//         <div class="profile-header">
//             <h2>${profile.name || 'No Name'}</h2>
//             <p class="email">${profile.email || 'No email'}</p>
//         </div>
//     `;
    
//     // Education section
//     if (profile.education && profile.education.length > 0) {
//         profileHTML += `
//             <div class="section">
//                 <h3>🎓 Education</h3>
//                 <div class="education-list">
//         `;
//         profile.education.forEach(edu => {
//             profileHTML += `
//                 <div class="education-item">
//                     <h4>${edu.institution || 'Unknown Institution'}</h4>
//                     <p class="degree">${edu.degree || ''}</p>
//                     <p class="year">${edu.year || ''}</p>
//                 </div>
//             `;
//         });
//         profileHTML += `</div></div>`;
//     }
    
//     // Work experience section
//     if (profile.work && profile.work.length > 0) {
//         profileHTML += `
//             <div class="section">
//                 <h3>💼 Work Experience</h3>
//                 <div class="work-list">
//         `;
//         profile.work.forEach(job => {
//             profileHTML += `
//                 <div class="work-item">
//                     <div class="work-header">
//                         <h4>${job.company || 'Unknown Company'}</h4>
//                         <span class="duration">${job.duration || ''}</span>
//                     </div>
//                     <p class="position">${job.position || ''}</p>
//                     <p class="description">${job.description || ''}</p>
//                 </div>
//             `;
//         });
//         profileHTML += `</div></div>`;
//     }
    
//     // Skills section
//     if (profile.skills && profile.skills.length > 0) {
//         profileHTML += `
//             <div class="section">
//                 <h3>🛠️ Skills</h3>
//                 <div class="skills-grid">
//         `;
//         profile.skills.forEach(skill => {
//             const skillName = skill.name || skill;
//             const proficiency = skill.proficiency ? `${skill.proficiency}%` : '';
            
//             profileHTML += `
//                 <div class="skill-item">
//                     <span class="skill-name">${skillName}</span>
//                     ${proficiency ? `<div class="skill-proficiency">
//                         <div class="proficiency-bar" style="width: ${skill.proficiency}%"></div>
//                         <span>${proficiency}</span>
//                     </div>` : ''}
//                 </div>
//             `;
//         });
//         profileHTML += `</div></div>`;
//     }
    
//     // Projects preview
//     if (profile.projects && profile.projects.length > 0) {
//         profileHTML += `
//             <div class="section">
//                 <h3>🚀 Projects Preview</h3>
//                 <div class="projects-preview">
//         `;
//         profile.projects.slice(0, 3).forEach(project => {
//             profileHTML += `
//                 <div class="project-preview">
//                     <h4>${project.title || 'Untitled Project'}</h4>
//                     <p>${project.description || 'No description'}</p>
//                     <a href="/projects" class="view-more">View all projects →</a>
//                 </div>
//             `;
//         });
//         profileHTML += `</div></div>`;
//     }
    
//     // Links section
//     if (profile.links && (profile.links.github || profile.links.linkedin || profile.links.portfolio)) {
//         profileHTML += `
//             <div class="section">
//                 <h3>🔗 Connect</h3>
//                 <div class="links">
//         `;
//         if (profile.links.github) {
//             profileHTML += `<a href="${profile.links.github}" target="_blank" class="social-link github">GitHub</a>`;
//         }
//         if (profile.links.linkedin) {
//             profileHTML += `<a href="${profile.links.linkedin}" target="_blank" class="social-link linkedin">LinkedIn</a>`;
//         }
//         if (profile.links.portfolio) {
//             profileHTML += `<a href="${profile.links.portfolio}" target="_blank" class="social-link portfolio">Portfolio</a>`;
//         }
//         profileHTML += `</div></div>`;
//     }
    
//     profileContent.innerHTML = profileHTML;
// }

// // Projects functions
// async function loadProjects() {
//     try {
//         showLoading('projects-content');
//         const urlParams = new URLSearchParams(window.location.search);
//         const skillFilter = urlParams.get('skill');
        
//         let url = `${API_BASE_URL}/projects`;
//         if (skillFilter) {
//             url += `?skill=${encodeURIComponent(skillFilter)}`;
//             document.getElementById('projects-title').textContent = `Projects - Filtered by: ${skillFilter}`;
//         }
        
//         const response = await fetch(url);
//         if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
//         const projects = await response.json();
//         appState.projects = projects;
//         displayProjects(projects);
//     } catch (error) {
//         console.error('Error loading projects:', error);
//         showError('Failed to load projects. Please try again later.');
//     }
// }

// function displayProjects(projects) {
//     const projectsContent = document.getElementById('projects-content');
    
//     if (!projects || projects.length === 0) {
//         projectsContent.innerHTML = `
//             <div class="card empty-state">
//                 <h3>No Projects Found</h3>
//                 <p>No projects are available at the moment.</p>
//                 <a href="/" class="btn-primary">Go Home</a>
//             </div>
//         `;
//         return;
//     }
    
//     let projectsHTML = `
//         <div class="projects-header">
//             <h2>${projects.length} Project${projects.length !== 1 ? 's' : ''}</h2>
//             <div class="filter-controls">
//                 <input type="text" id="project-search" placeholder="Search projects..." onkeyup="filterProjects()">
//             </div>
//         </div>
//         <div class="projects-grid">
//     `;
    
//     projects.forEach(project => {
//         projectsHTML += `
//             <div class="project-card" data-skills="${project.skills ? project.skills.join(',').toLowerCase() : ''}">
//                 <div class="project-header">
//                     <h3>${project.title || 'Untitled Project'}</h3>
//                     ${project.links && project.links.github ? 
//                         `<a href="${project.links.github}" target="_blank" class="project-link">GitHub</a>` : ''}
//                 </div>
//                 <p class="project-description">${project.description || 'No description available.'}</p>
                
//                 ${project.skills && project.skills.length > 0 ? `
//                     <div class="project-skills">
//                         ${project.skills.map(skill => 
//                             `<span class="skill-tag" onclick="filterBySkill('${skill}')">${skill}</span>`
//                         ).join('')}
//                     </div>
//                 ` : ''}
                
//                 ${project.links && (project.links.live || project.links.demo) ? `
//                     <div class="project-actions">
//                         ${project.links.live ? 
//                             `<a href="${project.links.live}" target="_blank" class="btn-secondary">Live Demo</a>` : ''}
//                     </div>
//                 ` : ''}
//             </div>
//         `;
//     });
    
//     projectsHTML += `</div>`;
//     projectsContent.innerHTML = projectsHTML;
// }

// function filterProjects() {
//     const searchTerm = document.getElementById('project-search').value.toLowerCase();
//     const projectCards = document.querySelectorAll('.project-card');
    
//     projectCards.forEach(card => {
//         const title = card.querySelector('h3').textContent.toLowerCase();
//         const description = card.querySelector('.project-description').textContent.toLowerCase();
//         const skills = card.getAttribute('data-skills') || '';
        
//         const matches = title.includes(searchTerm) || 
//                        description.includes(searchTerm) || 
//                        skills.includes(searchTerm);
        
//         card.style.display = matches ? 'block' : 'none';
//     });
// }

// function filterBySkill(skill) {
//     window.location.href = `/projects?skill=${encodeURIComponent(skill)}`;
// }

// // Search functions
// function setupSearch() {
//     const searchForm = document.getElementById('search-form');
//     if (searchForm) {
//         searchForm.addEventListener('submit', function(e) {
//             e.preventDefault();
//             const query = document.getElementById('search-query').value.trim();
//             if (query) {
//                 performSearch(query);
//             }
//         });
//     }
// }

// async function loadTopSkills() {
//     try {
//         const response = await fetch(`${API_BASE_URL}/skills/top?limit=10`);
//         if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
//         const skills = await response.json();
//         displayTopSkills(skills);
//     } catch (error) {
//         console.error('Error loading skills:', error);
//     }
// }

// function displayTopSkills(skills) {
//     const skillsContent = document.getElementById('skills-content');
    
//     if (!skills || skills.length === 0) {
//         skillsContent.innerHTML = '<p>No skills available.</p>';
//         return;
//     }
    
//     let skillsHTML = '<div class="top-skills">';
//     skills.forEach(skill => {
//         const skillName = skill.name || skill;
//         skillsHTML += `
//             <span class="skill-tag large" onclick="document.getElementById('search-query').value='${skillName}'; performSearch('${skillName}')">
//                 ${skillName}
//             </span>
//         `;
//     });
//     skillsHTML += '</div>';
//     skillsContent.innerHTML = skillsHTML;
// }

// async function performSearch(query) {
//     if (!query) return;
    
//     try {
//         showLoading('search-results');
//         const response = await fetch(`${API_BASE_URL}/search?q=${encodeURIComponent(query)}`);
//         if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
//         const results = await response.json();
//         displaySearchResults(results, query);
//     } catch (error) {
//         console.error('Error performing search:', error);
//         showError('Search failed. Please try again later.');
//     }
// }

// function displaySearchResults(results, query) {
//     const searchResults = document.getElementById('search-results');
    
//     let resultsHTML = `
//         <div class="search-header">
//             <h2>Search Results for "${query}"</h2>
//             <p class="results-count">Found ${calculateTotalResults(results)} results</p>
//         </div>
//     `;
    
//     if (Object.keys(results.profile).length === 0 && 
//         results.projects.length === 0 && 
//         results.skills.length === 0) {
//         resultsHTML += `
//             <div class="card empty-state">
//                 <h3>No results found</h3>
//                 <p>Try searching for something else.</p>
//             </div>
//         `;
//         searchResults.innerHTML = resultsHTML;
//         return;
//     }
    
//     // Profile results
//     if (Object.keys(results.profile).length > 0) {
//         resultsHTML += `
//             <div class="search-section">
//                 <h3>👤 Profile Matches</h3>
//                 <div class="card">
//         `;
//         for (const [field, value] of Object.entries(results.profile)) {
//             resultsHTML += `<p><strong>${field}:</strong> ${JSON.stringify(value)}</p>`;
//         }
//         resultsHTML += `</div></div>`;
//     }
    
//     // Project results
//     if (results.projects.length > 0) {
//         resultsHTML += `
//             <div class="search-section">
//                 <h3>🚀 Project Matches (${results.projects.length})</h3>
//                 <div class="projects-grid compact">
//         `;
//         results.projects.forEach(project => {
//             resultsHTML += `
//                 <div class="project-card">
//                     <h4>${project.title}</h4>
//                     <p>${project.description}</p>
//                 </div>
//             `;
//         });
//         resultsHTML += `</div></div>`;
//     }
    
//     // Skill results
//     if (results.skills.length > 0) {
//         resultsHTML += `
//             <div class="search-section">
//                 <h3>🛠️ Skill Matches (${results.skills.length})</h3>
//                 <div class="skills-list">
//         `;
//         results.skills.forEach(skill => {
//             const skillName = skill.name || skill;
//             resultsHTML += `<span class="skill-tag">${skillName}</span>`;
//         });
//         resultsHTML += `</div></div>`;
//     }
    
//     searchResults.innerHTML = resultsHTML;
// }

// function calculateTotalResults(results) {
//     let total = 0;
//     total += Object.keys(results.profile).length;
//     total += results.projects.length;
//     total += results.skills.length;
//     return total;
// }

// // Utility functions
// function showLoading(elementId) {
//     const element = document.getElementById(elementId);
//     if (element) {
//         element.innerHTML = `
//             <div class="loading">
//                 <div class="spinner"></div>
//                 <p>Loading...</p>
//             </div>
//         `;
//     }
// }

// function showError(message) {
//     const errorDiv = document.createElement('div');
//     errorDiv.className = 'error-message';
//     errorDiv.innerHTML = `
//         <span>❌</span>
//         <p>${message}</p>
//         <button onclick="this.parentElement.remove()">×</button>
//     `;
    
//     const container = document.querySelector('.container');
//     container.insertBefore(errorDiv, container.firstChild);
    
//     setTimeout(() => {
//         if (errorDiv.parentElement) {
//             errorDiv.remove();
//         }
//     }, 5000);
// }




const API_BASE_URL = window.location.origin + '/api';

// Global state
let appState = {
    profile: null,
    projects: [],
    skills: []
};

document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // Load data based on current page
    if (document.getElementById('profile-content')) {
        loadProfile();
    } else if (document.getElementById('projects-content')) {
        loadProjects();
    } else if (document.getElementById('search-content')) {
        setupSearch();
        loadTopSkills(); // This will load and display top skills
    }
    
    // Add active class to current page in navigation
    highlightCurrentPage();
}

function highlightCurrentPage() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

// Profile functions
async function loadProfile() {
    try {
        showLoading('profile-content');
        const response = await fetch(`${API_BASE_URL}/profile`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const profile = await response.json();
        appState.profile = profile;
        displayProfile(profile);
    } catch (error) {
        console.error('Error loading profile:', error);
        showError('Failed to load profile. Please try again later.');
    }
}

function displayProfile(profile) {
    const profileContent = document.getElementById('profile-content');
    
    if (!profile) {
        profileContent.innerHTML = `
            <div class="card error-card">
                <h3>No Profile Data</h3>
                <p>Profile data is not available. Please check if the database is seeded properly.</p>
            </div>
        `;
        return;
    }
    
    let profileHTML = `
        <div class="profile-header">
            <h2>${profile.name || 'No Name'}</h2>
            <p class="email">${profile.email || 'No email'}</p>
            <p class="location">${profile.location || ''}</p>
            <p class="phone">${profile.phone || ''}</p>
            <p class="title">${profile.title || ''}</p>
        </div>
        
        <div class="bio-section">
            <p>${profile.bio || ''}</p>
        </div>
    `;
    
    // Education section
    if (profile.education && profile.education.length > 0) {
        profileHTML += `
            <div class="section">
                <h3>🎓 Education</h3>
                <div class="education-list">
        `;
        profile.education.forEach(edu => {
            profileHTML += `
                <div class="education-item">
                    <h4>${edu.institution || 'Unknown Institution'}</h4>
                    <p class="degree">${edu.degree || ''}</p>
                    <p class="year">${edu.year || ''}</p>
                    ${edu.cgpa ? `<p class="cgpa">CGPA: ${edu.cgpa}</p>` : ''}
                </div>
            `;
        });
        profileHTML += `</div></div>`;
    }
    
    // Work experience section
    if (profile.work && profile.work.length > 0) {
        profileHTML += `
            <div class="section">
                <h3>💼 Work Experience</h3>
                <div class="work-list">
        `;
        profile.work.forEach(job => {
            profileHTML += `
                <div class="work-item">
                    <div class="work-header">
                        <h4>${job.company || 'Unknown Company'}</h4>
                        <span class="duration">${job.duration || ''}</span>
                    </div>
                    <p class="position">${job.position || ''}</p>
                    <p class="description">${job.description || ''}</p>
                </div>
            `;
        });
        profileHTML += `</div></div>`;
    }
    
    // Skills section - FIXED: Properly display skills with categories
    if (profile.skills && profile.skills.length > 0) {
        // Group skills by category
        const skillsByCategory = {};
        profile.skills.forEach(skill => {
            const category = skill.category || 'Other';
            if (!skillsByCategory[category]) {
                skillsByCategory[category] = [];
            }
            skillsByCategory[category].push(skill);
        });
        
        profileHTML += `
            <div class="section">
                <h3>🛠️ Skills</h3>
        `;
        
        // Display skills by category
        for (const [category, skills] of Object.entries(skillsByCategory)) {
            profileHTML += `
                <div class="skill-category">
                    <h4>${category}</h4>
                    <div class="skills-grid">
            `;
            
            skills.forEach(skill => {
                const skillName = skill.name || skill;
                const proficiency = skill.proficiency ? `${skill.proficiency}%` : '';
                
                profileHTML += `
                    <div class="skill-item">
                        <span class="skill-name">${skillName}</span>
                        ${proficiency ? `<div class="skill-proficiency">
                            <div class="proficiency-bar" style="width: ${skill.proficiency}%"></div>
                            <span>${proficiency}</span>
                        </div>` : ''}
                    </div>
                `;
            });
            
            profileHTML += `</div></div>`;
        }
        
        profileHTML += `</div>`;
    }
    
    // Projects preview
    if (profile.projects && profile.projects.length > 0) {
        profileHTML += `
            <div class="section">
                <h3>🚀 Projects Preview</h3>
                <div class="projects-preview">
        `;
        profile.projects.slice(0, 3).forEach(project => {
            profileHTML += `
                <div class="project-preview">
                    <h4>${project.title || 'Untitled Project'}</h4>
                    <p>${project.description || 'No description'}</p>
                    <a href="/projects" class="view-more">View all projects →</a>
                </div>
            `;
        });
        profileHTML += `</div></div>`;
    }
    
    // Certifications section
    if (profile.certifications && profile.certifications.length > 0) {
        profileHTML += `
            <div class="section">
                <h3>📜 Certifications</h3>
                <div class="certifications-list">
        `;
        profile.certifications.forEach(cert => {
            profileHTML += `
                <div class="certification-item">
                    <h4>${cert.name || 'Unknown Certification'}</h4>
                    <p class="issuer">${cert.issuer || ''} • ${cert.year || ''}</p>
                </div>
            `;
        });
        profileHTML += `</div></div>`;
    }
    
    // Links section
    if (profile.links) {
        profileHTML += `
            <div class="section">
                <h3>🔗 Connect</h3>
                <div class="social-links">
        `;
        if (profile.links.github) {
            profileHTML += `<a href="${profile.links.github}" target="_blank" class="social-link github">GitHub</a>`;
        }
        if (profile.links.linkedin) {
            profileHTML += `<a href="${profile.links.linkedin}" target="_blank" class="social-link linkedin">LinkedIn</a>`;
        }
        if (profile.links.portfolio) {
            profileHTML += `<a href="${profile.links.portfolio}" target="_blank" class="social-link portfolio">Portfolio</a>`;
        }
        profileHTML += `</div></div>`;
    }
    
    profileContent.innerHTML = profileHTML;
}

// Projects functions
async function loadProjects() {
    try {
        showLoading('projects-content');
        const urlParams = new URLSearchParams(window.location.search);
        const skillFilter = urlParams.get('skill');
        
        let url = `${API_BASE_URL}/projects`;
        if (skillFilter) {
            url += `?skill=${encodeURIComponent(skillFilter)}`;
            document.getElementById('projects-title').textContent = `Projects - Filtered by: ${skillFilter}`;
        }
        
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
        const projects = await response.json();
        appState.projects = projects;
        displayProjects(projects);
    } catch (error) {
        console.error('Error loading projects:', error);
        showError('Failed to load projects. Please try again later.');
    }
}

function displayProjects(projects) {
    const projectsContent = document.getElementById('projects-content');
    
    if (!projects || projects.length === 0) {
        projectsContent.innerHTML = `
            <div class="card empty-state">
                <h3>No Projects Found</h3>
                <p>No projects are available at the moment.</p>
                <a href="/" class="btn-primary">Go Home</a>
            </div>
        `;
        return;
    }
    
    let projectsHTML = `
        <div class="projects-header">
            <h2>${projects.length} Project${projects.length !== 1 ? 's' : ''}</h2>
            <div class="filter-controls">
                <input type="text" id="project-search" placeholder="Search projects..." onkeyup="filterProjects()">
            </div>
        </div>
        <div class="projects-grid">
    `;
    
    projects.forEach(project => {
        const skills = project.skills || [];
        projectsHTML += `
            <div class="project-card" data-skills="${skills.join(',').toLowerCase()}">
                <div class="project-header">
                    <h3>${project.title || 'Untitled Project'}</h3>
                    ${project.links && project.links.github ? 
                        `<a href="${project.links.github}" target="_blank" class="project-link">GitHub</a>` : ''}
                </div>
                <p class="project-description">${project.description || 'No description available.'}</p>
                
                ${skills.length > 0 ? `
                    <div class="project-skills">
                        ${skills.map(skill => 
                            `<span class="skill-tag" onclick="filterBySkill('${skill}')">${skill}</span>`
                        ).join('')}
                    </div>
                ` : ''}
                
                ${project.achievements && project.achievements.length > 0 ? `
                    <div class="project-achievements">
                        <h4>Achievements:</h4>
                        <ul>
                            ${project.achievements.map(achievement => 
                                `<li>${achievement}</li>`
                            ).join('')}
                        </ul>
                    </div>
                ` : ''}
                
                ${project.links && (project.links.live || project.links.demo) ? `
                    <div class="project-actions">
                        ${project.links.live ? 
                            `<a href="${project.links.live}" target="_blank" class="btn-secondary">Live Demo</a>` : ''}
                    </div>
                ` : ''}
            </div>
        `;
    });
    
    projectsHTML += `</div>`;
    projectsContent.innerHTML = projectsHTML;
}

function filterProjects() {
    const searchTerm = document.getElementById('project-search').value.toLowerCase();
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        const title = card.querySelector('h3').textContent.toLowerCase();
        const description = card.querySelector('.project-description').textContent.toLowerCase();
        const skills = card.getAttribute('data-skills') || '';
        
        const matches = title.includes(searchTerm) || 
                       description.includes(searchTerm) || 
                       skills.includes(searchTerm);
        
        card.style.display = matches ? 'block' : 'none';
    });
}

function filterBySkill(skill) {
    window.location.href = `/projects?skill=${encodeURIComponent(skill)}`;
}

// Search functions
function setupSearch() {
    const searchForm = document.getElementById('search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const query = document.getElementById('search-query').value.trim();
            if (query) {
                performSearch(query);
            }
        });
    }
    
    // Load top skills when search page loads
    loadTopSkills();
}

async function loadTopSkills() {
    try {
        showLoading('skills-content');
        const response = await fetch(`${API_BASE_URL}/skills/top?limit=20`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
        const skills = await response.json();
        displayTopSkills(skills);
    } catch (error) {
        console.error('Error loading skills:', error);
        document.getElementById('skills-content').innerHTML = `
            <div class="error-message">
                <span>❌</span>
                <p>Failed to load skills. Please try again later.</p>
            </div>
        `;
    }
}

function displayTopSkills(skills) {
    const skillsContent = document.getElementById('skills-content');
    
    if (!skills || skills.length === 0) {
        skillsContent.innerHTML = '<p class="no-skills">No skills available.</p>';
        return;
    }
    
    let skillsHTML = `
        <div class="top-skills-header">
            <h3>Top ${skills.length} Skills</h3>
            <p>Click any skill to search for it</p>
        </div>
        <div class="top-skills-grid">
    `;
    
    skills.forEach(skill => {
        const skillName = typeof skill === 'object' ? skill.name : skill;
        const proficiency = skill.proficiency ? `${skill.proficiency}%` : '';
        
        skillsHTML += `
            <div class="top-skill-item" onclick="document.getElementById('search-query').value='${skillName}'; performSearch('${skillName}')">
                <span class="top-skill-name">${skillName}</span>
                ${proficiency ? `
                    <div class="top-skill-proficiency">
                        <div class="proficiency-bar" style="width: ${skill.proficiency}%"></div>
                        <span class="proficiency-text">${proficiency}</span>
                    </div>
                ` : ''}
            </div>
        `;
    });
    
    skillsHTML += '</div>';
    skillsContent.innerHTML = skillsHTML;
}

async function performSearch(query) {
    if (!query) return;
    
    try {
        showLoading('search-results');
        const response = await fetch(`${API_BASE_URL}/search?q=${encodeURIComponent(query)}`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
        const results = await response.json();
        displaySearchResults(results, query);
    } catch (error) {
        console.error('Error performing search:', error);
        showError('Search failed. Please try again later.');
    }
}

function displaySearchResults(results, query) {
    const searchResults = document.getElementById('search-results');
    
    let resultsHTML = `
        <div class="search-header">
            <h2>Search Results for "${query}"</h2>
            <p class="results-count">Found ${calculateTotalResults(results)} results</p>
        </div>
    `;
    
    if (Object.keys(results.profile).length === 0 && 
        results.projects.length === 0 && 
        results.skills.length === 0) {
        resultsHTML += `
            <div class="card empty-state">
                <h3>No results found</h3>
                <p>Try searching for something else.</p>
            </div>
        `;
        searchResults.innerHTML = resultsHTML;
        return;
    }
    
    // Profile results
    if (Object.keys(results.profile).length > 0) {
        resultsHTML += `
            <div class="search-section">
                <h3>👤 Profile Matches</h3>
                <div class="card">
        `;
        for (const [field, value] of Object.entries(results.profile)) {
            if (Array.isArray(value)) {
                resultsHTML += `<p><strong>${field}:</strong> ${value.length} items found</p>`;
            } else {
                resultsHTML += `<p><strong>${field}:</strong> ${value}</p>`;
            }
        }
        resultsHTML += `</div></div>`;
    }
    
    // Project results
    if (results.projects.length > 0) {
        resultsHTML += `
            <div class="search-section">
                <h3>🚀 Project Matches (${results.projects.length})</h3>
                <div class="projects-grid compact">
        `;
        results.projects.forEach(project => {
            resultsHTML += `
                <div class="project-card">
                    <h4>${project.title}</h4>
                    <p>${project.description}</p>
                </div>
            `;
        });
        resultsHTML += `</div></div>`;
    }
    
    // Skill results
    if (results.skills.length > 0) {
        resultsHTML += `
            <div class="search-section">
                <h3>🛠️ Skill Matches (${results.skills.length})</h3>
                <div class="skills-list">
        `;
        results.skills.forEach(skill => {
            const skillName = typeof skill === 'object' ? skill.name : skill;
            resultsHTML += `<span class="skill-tag">${skillName}</span>`;
        });
        resultsHTML += `</div></div>`;
    }
    
    searchResults.innerHTML = resultsHTML;
}

function calculateTotalResults(results) {
    let total = 0;
    total += Object.keys(results.profile).length;
    total += results.projects.length;
    total += results.skills.length;
    return total;
}

// Utility functions
function showLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>Loading...</p>
            </div>
        `;
    }
}

function showError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.innerHTML = `
        <span>❌</span>
        <p>${message}</p>
        <button onclick="this.parentElement.remove()">×</button>
    `;
    
    const container = document.querySelector('.container');
    container.insertBefore(errorDiv, container.firstChild);
    
    setTimeout(() => {
        if (errorDiv.parentElement) {
            errorDiv.remove();
        }
    }, 5000);
}