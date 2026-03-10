from django.db.models import Q


class HtmxTableMixin:
    """
    Mixin for Django ListView that adds server-side search, ordering, and
    pagination via HTMX. Consuming apps mix this in with ListView:

        class MyListView(HtmxTableMixin, ListView):
            model = MyModel
            template_name = 'lazycrud/object_list.html'
            fields = ['name', 'created_at']
            search_fields = ['name', 'notes']
            orderable_fields = ['name', 'created_at']
            default_ordering = '-created_at'

    HTMX must be included in the project's base template.
    URL params: ?q=<search>&o=<field>&page=<n>
    """

    paginate_by = 25
    search_fields = []       # Fields to search with icontains
    orderable_fields = None  # None = use self.fields; [] = disable sorting
    default_ordering = None  # e.g. 'name' or '-created_at'
    htmx_template_name = 'lazycrud/_htmx_table_partial.html'

    def get_queryset(self):
        qs = super().get_queryset()

        q = self.request.GET.get('q', '').strip()
        if q and self.search_fields:
            query = Q()
            for field in self.search_fields:
                query |= Q(**{f'{field}__icontains': q})
            qs = qs.filter(query)

        o = self.request.GET.get('o', '')
        allowed = self._get_orderable_fields()
        if o and o.lstrip('-') in allowed:
            qs = qs.order_by(o)
        elif self.default_ordering:
            qs = qs.order_by(self.default_ordering)

        return qs

    def _get_orderable_fields(self):
        if self.orderable_fields is None:
            return list(getattr(self, 'fields', []))
        return self.orderable_fields

    def get_template_names(self):
        if self.request.headers.get('HX-Request'):
            return [self.htmx_template_name]
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['search_query'] = self.request.GET.get('q', '')
        ctx['current_ordering'] = self.request.GET.get('o', self.default_ordering or '')
        ctx['orderable_fields'] = self._get_orderable_fields()
        return ctx
