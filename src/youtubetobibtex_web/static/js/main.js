/*
youtubetobibtex_web - Export bibtex from youtube videos online
Copyright (C) 2020 Yoann Piétri

youtubetobibtex_web is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

youtubetobibtex_web is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with youtubetobibtex_web. If not, see <https://www.gnu.org/licenses/>.
*/

// Main js file for youtubetobibtex_web

// Tooltip

function resetTooltip(tooltipID) {
    var tooltip = document.getElementById(tooltipID);
    tooltip.innerHTML = "Copy";
}

// Textarea

function adjust(element) {
    element.style.height = "1px";
    element.style.height = (25 + element.scrollHeight) + "px";
}

// Copy

function copy(copyID, tooltipID) {
    var toCopy = document.getElementById(copyID);
    toCopy.select();
    toCopy.setSelectionRange(0, 99999);
    document.execCommand("copy");

    var tooltip = document.getElementById(tooltipID);
    tooltip.innerHTML = "Copied to clipboard !";
}

// Legals

function toggleLegals() {
    var legals = document.getElementById("footer-legals");
    if (legals.style.display === "block") {
        legals.style.display = "none";
        legals.style.opacity = 0;
    } else {
        legals.style.display = "block";
        legals.style.opacity = 1;
    }
}

// Initial

var textarea = document.getElementById("bibtex");
if (textarea !== null) {
    adjust(textarea);
}

// Listeners

var copyButton = document.getElementById("copy-button");
if (copyButton !== null) {
    copyButton.addEventListener('click', function () {
        copy('bibtex', 'tooltip');
    });
    copyButton.addEventListener('mouseout', function () {
        resetTooltip('tooltip');
    });
}

var legalsButton = document.getElementById("legals-button");
legalsButton.addEventListener('click', function () {
    toggleLegals();
});

document.querySelectorAll(".message-close").forEach(item => {
    item.addEventListener('click', function () {
        var parent = item.parentNode;
        parent.style.display = "none";
    });
});