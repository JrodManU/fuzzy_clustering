from fuzzywuzzy import fuzz
import datetime

# sqlite3 connection (conn) and suggestion is formated as a tuple:
# (name, date, customer_name)
def process_suggestion(conn, new_suggestion):
    #cutoff refers to how similar items have to be in be in the same group
    cutoff = 85
    best_ratio_average = 0
    best_group_id = 0

    sql = '''SELECT id FROM suggestion_groups'''
    c_groups = conn.cursor()
    c_groups.execute(sql)
    for group in c_groups:
    #####
        ratio_sum = 0
        row_count = 0

        sql = '''SELECT suggestions.name, suggestion_groups.id
                    FROM suggestion_groups INNER JOIN suggestions
                    ON suggestion_groups.id = ? AND
                    suggestion_groups.id = suggestions.group_id'''
        c_suggestions = conn.cursor()
        #group is a tuple like (id)
        c_suggestions.execute(sql, group)
        print("")
        for suggestion in c_suggestions:
        #####
            print("new: " + str(new_suggestion) + " in_group: " + str(suggestion))
            # both of these tuples have suggestions.name as their first item
            # using token_sort instead of just ratio since it could be multiword
            ratio = fuzz.token_sort_ratio(new_suggestion[0], suggestion[0])
            ratio_sum += ratio
            row_count += 1
            print(ratio)
        #####
        ratio_average = ratio_sum / row_count
        print("ratio_average: " + ratio_average)
        if ratio_average > best_ratio_average:
            best_ratio_average = ratio_average
            best_group_id = group[0]
    #####
    if(best_ratio_average > cutoff):
        new_suggestion = (best_group_id,) + new_suggestion
    else:
        #since execute likes tuples
        new_group_data = (str(datetime.datetime.now()),)
        sql = '''INSERT INTO suggestion_groups (date_added) VALUES(?)'''
        c_new_group = conn.cursor()
        c_new_group.execute(sql, new_group_data)
        #lastrowid will return the id of the new group we made
        new_suggestion = (c_new_group.lastrowid,) + new_suggestion

    sql = "INSERT INTO suggestions(group_id, name, date, customer_name) VALUES(?,?,?,?)"
    c_new_suggestion = conn.cursor()
    c_new_suggestion.execute(sql, new_suggestion)

    #save all changes we made to the database
    conn.commit()
