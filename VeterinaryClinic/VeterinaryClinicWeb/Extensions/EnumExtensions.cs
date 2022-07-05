using Microsoft.AspNetCore.Mvc.Rendering;

namespace VeterinaryClinicWeb.Extensions
{
    public static class EnumExtensions
    {
        public static SelectList GetSelectList<T>(object selectedValue = null)
        {
            var values = Enum.GetValues(typeof(T));
            var items = new List<SelectListItem>(values.Length);

            foreach(var value in values)
                items.Add(new(value.ToString(), value.ToString()));

            return new SelectList(items, "Text", "Value", selectedValue);
        }
    }
}
