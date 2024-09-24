function submitToggle() {
    const selectedRole = document.querySelector('input[name="role"]:checked').value;

    // Redirect based on the selected role
    if (selectedRole === 'parent') {
        window.location.href = '/templates/parent/register-parent.html';
    } else if (selectedRole === 'teacher') {
        window.location.href = '/templates/teacher/register-teacher.html';
    } else if (selectedRole === 'student') {
        window.location.href = '/templates/student/register-student.html';
    }
}