# Postmortem

This project contains tasks for learning about writing a postmortem.

## Tasks To Complete

+ [x] 0. My first postmortem<br/>_**[Blog_Post.md](Blog_Post.md)**_ contains a blog post that meets the following requirements:
  + **INFO:**
    + Using one of the web stack debugging project issues or an outage you have personally faced, write a postmortem. If you have not experienced an outage, feel free to create a fictional scenario.
    + While postmortem formats can vary, stick to this one to ensure proper review by your peers.
  + **Requirements:**
    + **Issue Summary** must contain:
      + Duration of the outage with start and end times (including timezone).
      + Impact (What service was down/slow? What were users experiencing? What percentage of users were affected?)
      + Root cause
    + **Timeline** (format: `time` - `brief description`) must contain:
      + When the issue was detected
      + How the issue was detected (monitoring alert, an engineer noticed something, a customer complained…)
      + Actions taken (what parts of the system were investigated, what were the assumptions on the root cause)
      + Misleading investigation/debugging paths
      + Which team/individuals the incident was escalated to
      + How the incident was resolved
    + **Root Cause and Resolution** must contain:
      + Detailed explanation of what caused the issue
      + Detailed explanation of how the issue was fixed
    + **Corrective and Preventative Measures** must contain:
      + Broadly speaking, what can be improved/fixed
      + A list of specific tasks to address the issue (e.g., patch Nginx server, add monitoring on server memory…)
      + Be brief and to the point (400-600 words)

+ [x] 1. Make people want to read your postmortem
  + In an age of information overload, it’s important to make your postmortem engaging.
  + Add humor, a pretty diagram, or anything else that will catch your audience's attention.
