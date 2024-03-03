python manage.py pre_mailing --pk_mailing=18
{% if object.mailing_status == 0 %}
        <td><span class="badge rounded-pill text-bg-warning">CREATED</span></td>
        {% elif object.mailing_status == 1 %}
        <td><span class="badge rounded-pill text-bg-secondary">ACTIVATING</span></td>
        {% elif object.mailing_status == 2 %}
        <td><span class="badge rounded-pill text-bg-danger">STOP</span></td>
        {% else %}
        <td><span class="badge rounded-pill text-bg-success">SUCCESS</span></td>
        {% endif %}
